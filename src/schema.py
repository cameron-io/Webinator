
sign_up = {
  "type": "object",
  "properties": {
    "username": { "type": "string" },
    "email": { "type": "string" },
    "password": { "type": "string" }
  },
  "required": ["username", "email", "password"]
}

login = {
  "type": "object",
  "properties": {
    "email": { "type": "string" },
    "password": { "type": "string" }
  },
  "required": ["email", "password"]
}
