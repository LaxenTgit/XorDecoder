<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=00FF9F&center=true&vCenter=true&width=600&lines=XorDecoder+LatenT;CTF+XOR+Analysis+Tool;Hex+%E2%86%92+XOR+%E2%86%92+Flag+Recovery" />
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-00ff9f?style=flat-square">
  <img src="https://img.shields.io/badge/ctf-xor_tool-111111?style=flat-square">
  <img src="https://img.shields.io/badge/status-stable-00ff9f?style=flat-square">
  <img src="https://img.shields.io/badge/license-MIT-888888?style=flat-square">
</p>

---

## XorDecoder

XorDecoder, CTF ortamlarında XOR tabanlı şifrelenmiş verileri çözmek için geliştirilmiş hafif bir analiz aracıdır.

Amaç, hex input üzerinden XOR çözümlemesi yaparak flag recovery sürecini otomatikleştirmektir.

---

## WORKFLOW

```
HEX INPUT
   ↓
bytes.fromhex()
   ↓
UTF-8 DECODE
   ↓
XOR DATA RECONSTRUCTION
   ↓
KEY GENERATION (THM PATTERN)
   ↓
REPEATING XOR DECRYPTION
   ↓
FLAG OUTPUT
```

---

## FEATURES

- Hex string parsing
- XOR data reconstruction
- Pattern-based key generation
- Repeating XOR decryption engine
- Terminal loading animations
- CTF-friendly output formatting

---

## CORE LOGIC

### Hex Decode

Input hex string byte array'e çevrilir:

```python
bytes.fromhex(hex_string).decode('utf-8')
```

---

### Key Generation

Sabit pattern tabanlı pseudo-key üretimi:

```python
keys = ['T', 'H', 'M', '{', '}']
```

Bu karakterler XOR işleminde kullanılarak key oluşturulur.

---

### Decryption

Repeating XOR mantığı:

```python
flag += chr(ord(xored_original[i]) ^ ord(key[i % len(key)]))
```

---

## USAGE

```bash
python main.py
```

### Input

```
68656c6c6f
```

---

## EXAMPLE OUTPUT

```text
📥 Hex string: 3e7f1b19495b563a0c4d2f4f22234d1e0335095a2b59245158067b2f0a6c18432f524c184f191044

✓ Hex decode tamamlandı!

🔍 XOR data: >[V:
                 M/O"#M5        Z+Y$QX{/
l▒C/RL▒OD

✓ Key generate tamamlandı!
🔑 Key: 'j7Vb9'

✓ Flag decrypt tamamlandı!

==================================================
🎉 FLAG: THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}
==================================================
```

---

## PROJECT STRUCTURE

```
XorDecoder/
├── main.py
└── requirements.txt
```

---

## REQUIREMENTS

```
colorama
```

Install:

```bash
pip install colorama
```

---

## LIMITATIONS

- Modern encryption (AES vb.) desteklemez
- Key recovery heuristic tabanlıdır
- False positive üretme ihtimali vardır
- Sadece CTF / eğitim amaçlı kullanım için uygundur

---

## THREAT MODEL

- Weak XOR implementations hedeflenir
- Repeating-key XOR varsayımı yapılır
- Real-world cryptographic security sağlamaz

---

## DISCLAIMER

Bu araç yalnızca eğitim amaçlı ve yetkili güvenlik test ortamlarında (CTF platformları: TryHackMe, HackTheBox vb.) kullanılmak üzere geliştirilmiştir.

---

## SIGNAL

```
[ OK ] HEX DECODE COMPLETE
[ OK ] XOR ANALYSIS COMPLETE
[ OK ] KEY GENERATED
[ OK ] FLAG RECOVERED
```
