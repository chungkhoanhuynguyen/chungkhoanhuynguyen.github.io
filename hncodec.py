# Đóng gói dữ liệu cho web: nén + xáo trộn, để người ngoài lấy link không đọc/copy thẳng được.
# Trang web giải mã bằng hàm HD trong index.html (cùng thuật toán). Chỉ là lớp che, không phải mã hoá bảo mật.
import json, zlib, os

_K = "hn-ck-2026-x7"


def _seed(name):
    h = 2166136261
    for ch in (_K + "|" + name).encode():
        h ^= ch
        h = (h * 16777619) & 0xFFFFFFFF
    return h or 1


def _xor(buf, name):
    s = _seed(name)
    out = bytearray(buf)
    for i in range(len(out)):
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= s >> 17
        s ^= (s << 5) & 0xFFFFFFFF
        out[i] ^= s & 0xFF
    return bytes(out)


def _name(path):
    return os.path.basename(path).rsplit(".", 1)[0]


def pack(obj, name):
    raw = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode()
    return _xor(zlib.compress(raw, 9), name)


def dump(obj, path):
    """Ghi file .bin; chỉ ghi khi nội dung đổi (tránh commit thừa). Trả về True nếu có ghi."""
    data = pack(obj, _name(path))
    try:
        if open(path, "rb").read() == data:
            return False
    except Exception:
        pass
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    open(path, "wb").write(data)
    return True


def load(path, default=None):
    try:
        return json.loads(zlib.decompress(_xor(open(path, "rb").read(), _name(path))))
    except Exception:
        return default


def drop(path):
    """Xoá bản JSON đọc được cũ (nếu còn) sau khi đã có bản .bin."""
    try:
        os.remove(path)
    except Exception:
        pass
