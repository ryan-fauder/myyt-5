import pickle
import struct
from .config import BUFFER_SIZE, PROTOCOL_HEADER_MAX_LEN, PROTOCOL_MESSAGE_MAX_LEN

class Protocol:
    def get_size(message: bytes) -> int:
        message_size, _ = struct.unpack_from(f"!{PROTOCOL_MESSAGE_MAX_LEN}ss", message)

        message_size = int(message_size.rstrip(b'\x00').decode().strip())
        return message_size

    def marshalMessage(body: any, type_message=None, status=None) -> bytes:
        body_serialized = pickle.dumps(body)
        body_size = len(body_serialized)
        header = {
            "type": type_message,
            "size": body_size,
            "status": status,
        }
        header_serialized = pickle.dumps(header)
        header_size = len(header_serialized)

        message_size = header_size + body_size + (PROTOCOL_HEADER_MAX_LEN + PROTOCOL_MESSAGE_MAX_LEN)
        message_size = (message_size + (BUFFER_SIZE - 1)) // BUFFER_SIZE * BUFFER_SIZE

        if len(str(header_size)) > PROTOCOL_HEADER_MAX_LEN or len(str(message_size)) > PROTOCOL_MESSAGE_MAX_LEN:
            raise ValueError("Tamanhos inválidos para o cabeçalho ou corpo da mensagem.")
        
        empty = message_size - (PROTOCOL_MESSAGE_MAX_LEN + PROTOCOL_HEADER_MAX_LEN + header_size + body_size)
        message = struct.pack(
             f"!{PROTOCOL_MESSAGE_MAX_LEN}s{PROTOCOL_HEADER_MAX_LEN}s{header_size}s{body_size}s{empty}s",
                                            str(message_size).encode(),
                                            str(header_size).encode(),
                                            header_serialized,
                                            body_serialized,
                                            b'\x00' * empty)
        return message
    
    @staticmethod
    def unmarshalMessage(message: bytes) -> any:
            offset = 0
            message_size, header_size = struct.unpack_from(f"!{PROTOCOL_MESSAGE_MAX_LEN}s{PROTOCOL_HEADER_MAX_LEN}s", message)

            message_size = int(message_size.rstrip(b'\x00').decode().strip())
            header_size = int(header_size.rstrip(b'\x00').decode().strip())
            offset += PROTOCOL_HEADER_MAX_LEN + PROTOCOL_MESSAGE_MAX_LEN

            header_serialized, _ = struct.unpack_from("" + str(header_size) + "ss", message, offset=offset)
            header = pickle.loads(header_serialized.rstrip(b'\x00'))

            offset += header_size
            body_size = header['size']
            body_serialized, _ = struct.unpack_from("" + str(body_size) + "ss", message, offset=offset)

            body = pickle.loads(body_serialized)
            return header, body
if __name__ == '__main__':
    data = {
        "name": "Alberto"
    }
    marshal = Protocol.marshalMessage(data)
    print(Protocol.get_size(marshal))
    print(Protocol.unmarshalMessage(marshal))