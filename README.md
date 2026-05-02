<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=00FF9F&center=true&vCenter=true&width=600&lines=XorDecoder+LATENT;CTF+XOR+Cryptanalysis+Tool;TryHackMe+%2F+HackTheBox+AndOthers" />
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-00ff9f?style=flat-square">
  <img src="https://img.shields.io/badge/ctf-tool-111111?style=flat-square">
  <img src="https://img.shields.io/badge/status-stable-00ff9f?style=flat-square">
  <img src="https://img.shields.io/badge/license-MIT-888888?style=flat-square">
</p>

---

## ▓▒░ XorDecoder ░▒▓

> Lightweight XOR cryptanalysis engine for CTF environments  
> Built for speed, pattern detection and automated key recovery

---

## SYSTEM CAPABILITIES

```
- Single-byte XOR brute force
- Repeating-key XOR analysis
- Key-length inference (1–30 range)
- Ranked output scoring system
- Hex / raw byte ingestion
```

---

## VISUAL WORKFLOW

<pre align="center">
INPUT → HEX DECODE → XOR ANALYSIS → KEY GUESSING → SCORING ENGINE → TOP RESULTS
</pre>

---

## CORE ENGINE

### Single Byte Attack
Brute force over 0–255 keyspace and evaluate plaintext probability.

### Multi Byte Attack
Column-based frequency analysis for repeating XOR keys.

---

## SCORING MODEL

Score = PrintableRatio + KeywordWeight + SpaceDistribution

Key indicators:
- printable ASCII density  
- CTF keyword hits (flag, thm, xor)  
- linguistic spacing patterns  

---

## USAGE

```bash
python xor_decoder.py
```

Input:
```text
68656c6c6f
```

Output:
```text
key: b'\x01'
output: hello
score: 2.87
```

---

## PROJECT STRUCTURE

```text
XorDecoder/
├── xor_decoder.py
├── requirements.txt
└── README.md
```

---

## REQUIREMENTS

```text
colorama
```

---

## COLLAPSIBLE DETAILS

<details>
<summary>Threat Model Notes</summary>

- Designed for CTF environments only  
- Assumes weak XOR implementations  
- Not suitable for modern cryptographic systems  

</details>

<details>
<summary>Limitations</summary>

- No AES / modern cipher support  
- Limited NLP-based validation  
- Heuristic scoring may produce false positives  

</details>

---

## DISCLAIMER

This tool is intended strictly for educational use and authorized security research environments (CTF platforms such as TryHackMe and HackTheBox).

---

## SIGNAL

```
[ OK ] XOR ENGINE INITIALIZED
[ OK ] ANALYSIS MODULE LOADED
[ OK ] READY FOR INPUT
```
