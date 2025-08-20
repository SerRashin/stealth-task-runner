# Steal Task Runner

## Запуск

```bash
cp .env.example .env
docker compose up --build
```

Проверка:

```bash
curl -X POST http://localhost:8000/run   -H "Content-Type: application/json"   --data @sample_payload.json
```

## Пример экшена капчи

```json
{
  "type": "recognize_captcha",
  "action": {
    "by": "css",
    "value": "#captchaImage",
    "recognize": "$captchaCode",
    "provider": "rucaptcha"
  }
}
```
