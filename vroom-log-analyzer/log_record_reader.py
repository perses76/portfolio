import re
import zlib
import s3

class LogglyRecordReader(object):
    def __init__(self, file_name, pattern_str):
        self.file_name = file_name
        self.buffer = ''
        self.pattern = re.complie(pattern_str)

    def get_records(self):
        for line in self.get_lines():
            if self.pattern.search(line):
                yield line

    def get_lines(self):
        buf = ''
        for chunk in self.get_decoded_chunks():
            prev_chunk = None
            st = 0
            for m in re.finditer(r'\n', chunk):
                line = chunk[st:m.start(0)]
                st = m.start(0) + 1
                if prev_chunk is not None:
                    yield buf + prev_chunk
                    buf = ''
                prev_chunk = line
            if prev_chunk is not None:
                yield prev_chunk
            buf = buf + chunk[st:len(chunk)]
        yield buf

    def get_decoded_chunks(self):
        dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
        for chunk in self.get_chunks():
            yield dec.decompress(chunk)

    def get_chunks(self):
        file_info = s3.get_object_info(self.file_name)
        total_size = int(file_info['content-length'])
        for idx in range(0, total_size, READ_SIZE):
            content = s3.load_file(self.file_name, bytes_range=(idx, idx + READ_SIZE - 1))
            yield content
