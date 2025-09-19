"""wp
两个文件都不能直接打开，去学了一下rsa加密
给了我们key文件，就是和ras的公钥和私钥有关，然后用私钥解密flag.enc就行
打开kali，使用penssl rsa -pubin -text -modulus -in '/var/run/vmblock-fuse/blockdir/EDfn9D/pub.key'
得到Exponent: 65537 (0x10001)
Modulus=C0332C5C64AE47182F6C1C876D42336910545A58F7EEFEFC0BCAAF5AF341CCDD


"""
hex_str = "C0332C5C64AE47182F6C1C876D42336910545A58F7EEFEFC0BCAAF5AF341CCDD"
decimal = int(hex_str, 16)
print(decimal)  # 输出：86934482296048119190666062003494800588905656017203025617216654058378322103517，即为n
#工具 https://www.dcode.fr/rsa-cipher
#接下来利用脚本得到p，q，然后用以下脚本解出flag
import gmpy2
import rsa

p = 285960468890451637935629440372639283459
q = 304008741604601924494328155975272418463
e = 65537
n = 86934482296048119190666062003494800588905656017203025617216654058378322103517

d = gmpy2.invert(e, (q - 1) * (p - 1))
print(d)

d = 81176168860169991027846870170527607562179635470395365333547868786951080991441

key = rsa.PrivateKey(n, e, d, p, q)
print(key)

# with open("flag.enc", "rb") as f:
#     print(rsa.decrypt(f.read(), key).decode())















