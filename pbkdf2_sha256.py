import hashlib
import hmac

def pbkdf2_sha256(password, salt, iterations, key_length):
    # Вычисляем длину блока хэша
    hash_length = hashlib.sha256().digest_size
    # Вычисляем количество блоков, необходимых для формирования ключа
    blocks_needed = -(-key_length // hash_length)
    # Инициализируем производную как пустую строку
    derived_key = b""
    
    for block_index in range(1, blocks_needed + 1):
        # Вычисляем INT_LE(i)
        block_index_bytes = bytearray((block_index >> 24, block_index >> 16, block_index >> 8, block_index & 0xff))
        # Инициализируем первый блок U1 как HMAC(P, S || INT_LE(i))
        u_block = hmac.new(password, salt + bytes(block_index_bytes), hashlib.sha256).digest()
        
        # Вычисляем последующие блоки U2, U3, ..., Uc
        for _ in range(iterations - 1):
            u_block = hmac.new(password, u_block, hashlib.sha256).digest()
        
        # Добавляем блок U1, U2, ..., Uc к производной
        derived_key += u_block
    
    # Усекаем результат до требуемой длины ключа
    return derived_key[:key_length]

# Получаем ввод пользователя для пароля
password = bytes(input("Введите пароль: "), 'utf-8')
salt = b"unique_salt"
iterations = 10000
key_length = 64  # Длина ключа в байтах

# Генерируем ключ
key = pbkdf2_sha256(password, salt, iterations, key_length)
print("Алгоритм PBKDF2_SHA256")
print("Количество итераций:", iterations)
print("Сгенерированный ключ (hex):", key.hex())
