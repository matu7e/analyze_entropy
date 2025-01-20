import math
import base64

def calculate_entropy(data):
    """Calcula la entropía Shannon de una cadena."""
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1
    entropy = -sum((freq / len(data)) * math.log2(freq / len(data)) for freq in frequency.values())
    return entropy

def analyze_token(token):
    """Analiza un token JWT completo, evaluando la entropía de cada parte."""
    try:
        # Dividir el token en sus partes: header, payload, signature
        header, payload, signature = token.split('.')
        
        # Decodificar las partes
        header_decoded = base64.urlsafe_b64decode(header + "==").decode("utf-8", "ignore")
        payload_decoded = base64.urlsafe_b64decode(payload + "==").decode("utf-8", "ignore")
        signature_decoded = base64.urlsafe_b64decode(signature + "==").decode("utf-8", "ignore")
        
        # Calcular la entropía de cada parte
        header_entropy = calculate_entropy(header_decoded)
        payload_entropy = calculate_entropy(payload_decoded)
        signature_entropy = calculate_entropy(signature_decoded)
        
        # Calcular la entropía total del token
        total_entropy = header_entropy + payload_entropy + signature_entropy
        
        return {
            "header_entropy": header_entropy,
            "payload_entropy": payload_entropy,
            "signature_entropy": signature_entropy,
            "total_entropy": total_entropy,
        }
    except Exception as e:
        return {"error": str(e)}

# Lista de tokens para analizar
tokens = [
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDc3NTAsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NTM1MCwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.vHITuLe93s9HWT84QPowlI1bjyANMwJXoRcnkIPPScQO6UmI2ZgOKri42e2lN4Jh_FE3p_Ivv-Tkjr0s_F4nGg",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3MTcsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjMxNywidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.xQXF0PPzDEQOYaO-lMCKHj-FSJS6YOHVmdnLsjlKuNFRkyJ1K6wGWj4kkzTQ4JRwPzzPqvfDseIL4jTLCq0nMA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3MjgsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjMyOCwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.K2SQC4t0W7ojqBjKxV-vNvcH6pAxO7QWxrtLVkhqre-wJD2kYPFiuGYGvjOW1fw3DBepIlsvGzrdgDlRb8dkOw",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3NTMsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjM1MywidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.pML4fw3aC8Tlmph2SnkKTAN5CpvLpPwNP7eu4Y0tm9GxZr1opy7Qi512A3lScCoSdoY9jN9cyOBMhbpZfpRIWA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3NjIsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjM2MiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.atzDc5e-4jfT4tvFYntUZGctmD9ZtIxpJN-XdFBTLwi193pDuyHhijh9LP8YJl9wXVQgG1MS6BiZHpkjH6wPOQ",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3NzIsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjM3MiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.R2qwv9vf6PgOQczuk2Xeqj4rFZKuR-fn6DZmcFopC7n19Ae_wqkujBLCgyRt2raRP3jErAs20-TH_e5gBS5NXQ",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3ODIsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjM4MiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.VPb6tjuvsb6RuUdess2Nrh4sjcsmWoU3W9XQ42VwqrArf0AG-4SDXGOqMAsIvwulVFmcgR_kuhSN7R4PkLODkQ",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg3OTMsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjM5MywidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.WM0KLgcQpJ_w--xDRMm96He6lfUmyh1_N3oE6OujDmpHuPf1dNm8GNiUEA7KfICJn38vtbuvQVbdzhXmo0dLuA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4MDYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQwNiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.ZAsQndQLSCeLeeM4k5xgBe7mAcZOeGlAMR5_7N67vEJ5PicfIruEy2SgsNKnPT3SetUa85oSiQnh_RnoQZ9nOQ",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4MTYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQxNiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.wZRyHYTNHIqDYP1aYPme1hT2J88dlLpK5FHGgxgFmLygqxXCh2IGX0ff8xfDblqt8HS8hFrgXe5gk4afED0i7Q",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4MjYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQyNiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.MfRMeDzuBDSu8y8NmlSeX7de6vNNfayB9TmNDDjoiJhM2bsQ1hw8t6PcD1gU2_v7cw4eNJKp0ZoAA7eO5G9q4Q",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4MzYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQzNiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.XbEERHyHxACzMlO4-coTcw0QiywplmNR8FJgQEl0yK8-uo2IhBLmI9gzlhIb_3ij-Zim8KBddCNVPq-5gJ9zCA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4NDYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ0NiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.VWlF9TNto0YvCL1Edbxb4nkTfHT2kq4OU1EZi2Ul5MVGRfkMnYeUGS1GPUrQwR_9G28Z7rEPqd7MF9owddcExw",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4NTUsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ1NSwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.xBdM_DzAV1WfesfqiNMQa6CdpnK0pkoaxyceUeyDW37WnQSkQtTJMCyL7P646HSIxF0-WPWR7vKOXQFHU3jSng",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4NjUsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ2NSwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.XVzjux3N1pXJff62Sn2Mh-VOIkgwzwCFeGPMc4XtaneheOmhIa7Q_dGHesDLeWgElOZTJuxtxVxXsaXaYTnYOg",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4NzYsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ3NiwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.ATU23syynr6BGeQQiYqIGARcNVvn39H8y7Fua9eIFN5j0p0HbsjLmU0vMoIhxDEnbQQFWc9QXW_yxp8avf5Q9g",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4ODcsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ4NywidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.MD5TVdVxGC8FhjnREVoB2y0rmqmzWv8kulrvRbPNp7UfcjirInqQHhlbg7XPHdXvWbFMHPTFlydtBF1RV1KmfA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg4OTUsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjQ5NSwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.O4yp-2XrPgwu5PQ4wcUpDjwhN7V2aXtCuWKEi8ZBPT3F2gLc3glMbWIjrhNtxsQi7mj-OMZ_4n2HPPVxi2kq3g",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg5MDQsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjUwNCwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.yNEFWeBUYnSpYwQqSRPNVgh5j7GmcBxsTiet-JnuuEt8j-IUV5Mtsmm9E3eieh-vEltEmGzJZyhvhDwbrNq7AQ",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDg5MTQsInN1YiI6IlJ1Z2VwcmVzYSIsImV4cCI6MTc2ODk2NjUxNCwidXN1YXJpbyI6IjIwNDMyNzExOTc5Iiwibm9tYnJlIjoiTWF0aWFzIEplc3VzIiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.2czzSsV2AZ3Pg3IvIk33aAeNiN155rMMJmswiwxpbwjJKL0Gfoju8AF9rLffb42gbHdVI-khA1f1tmLv4tcb6Q"
]

# Variables para el promedio de entropía
total_header_entropy = 0
total_payload_entropy = 0
total_signature_entropy = 0
total_total_entropy = 0
total_tokens = len(tokens)

# Analizar cada token y acumular la entropía
for i, token in enumerate(tokens, 1):
    print(f"\nAnalizando Token {i}...")
    result = analyze_token(token)

    if "error" in result:
        print(f"Error analizando el token: {result['error']}")
    else:
        print(f"Entropía del Header: {result['header_entropy']:.2f} bits")
        print(f"Entropía del Payload: {result['payload_entropy']:.2f} bits")
        print(f"Entropía de la Firma: {result['signature_entropy']:.2f} bits")
        print(f"Entropía total del Token: {result['total_entropy']:.2f} bits")
        
        total_header_entropy += result['header_entropy']
        total_payload_entropy += result['payload_entropy']
        total_signature_entropy += result['signature_entropy']
        total_total_entropy += result['total_entropy']

# Calcular el promedio de entropía
average_header_entropy = total_header_entropy / total_tokens
average_payload_entropy = total_payload_entropy / total_tokens
average_signature_entropy = total_signature_entropy / total_tokens
average_total_entropy = total_total_entropy / total_tokens

# Mostrar el promedio de entropía
print("="*100)
print("Promedio de Entropía por Token:")
print("="*100)
print(f"Entropía promedio del Header: {average_header_entropy:.2f} bits")
print(f"Entropía promedio del Payload: {average_payload_entropy:.2f} bits")
print(f"Entropía promedio de la Firma: {average_signature_entropy:.2f} bits")
print("="*100)
print(f"Entropía promedio total del Token: {average_total_entropy:.2f} bits")
print("="*100)

# Verificar si pasa la prueba
if average_total_entropy >= 64:
    print("APROBADO V3.2.2 - Entropía de 64 bits en los tokens de sesión")
    print("="*100)
else:
    print("DESAPROBADO V3.2.2 - Entropía de 64 bits en los tokens de sesión")
    print("="*100)
