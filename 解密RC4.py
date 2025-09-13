def rc4(key, data):
    # 初始化 S 算法状态表
    S = list(range(256))
    j = 0
    key_len = len(key)

    # 初始化 S 表
    for i in range(256):
        j = (j + S[i] + key[i % key_len]) % 256
        S[i], S[j] = S[j], S[i]

    # 加密/解密数据
    i = 0
    j = 0
    result = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)

    return bytes(result)


def decrypt_file(key, input_file):
    # 将密钥转换为字节形式
    key_bytes = key.encode('utf-8')
    # 读取加密文件
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    print(encrypted_data)
    # 使用 RC4 解密文件内容
    decrypted_data = rc4(key_bytes, encrypted_data)

    # 将解密后的内容输出到控制台
    print("解密后的内容：")
    print(decrypted_data.decode('utf-8', errors='ignore'))


# 解密 enflag.txt 文件并输出结果
key=input("请输入密钥：")
decrypt_file(key, "Ciphertext.txt")