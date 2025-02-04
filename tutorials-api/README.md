# Telegram Bot API

## Resources

## Coding

> NOTE: not case-sensitive i.e. getMe or getme

- Check status of Bot: <https://api.telegram.org/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/getUpdates>

```json
{
  "ok":true,
  "result":[]
}
```

Now, you can send a message to the TG bot from chat. And when you reload the page, you get 1st element in `result` array.

> NOTE: to get the updates run it from 1 server at a time. Just close the terminal (if running an instance there), cloud. Then the above url would give response like this:

<details>
<summary><b>Expand: </b></summary>

```json
{
  "ok": true,
  "result": [
    {
      "update_id": 56245526,
      "message": {
        "message_id": 469,
        "from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "chat": {
          "id": 410894301,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "type": "private"
        },
        "date": 1621282658,
        "text": "/showkycinfo",
        "entities": [
          {
            "offset": 0,
            "length": 12,
            "type": "bot_command"
          }
        ]
      }
    },
    {
      "update_id": 56245527,
      "message": {
        "message_id": 470,
        "from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "chat": {
          "id": 410894301,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "type": "private"
        },
        "date": 1621282683,
        "forward_from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "forward_date": 1621265481,
        "photo": [
          {
            "file_id": "AgACAgUAAxkBAAIB1mCiz3sYjDHgE7goA5ckC9lRJow7AAISrDEbtQ4YVUGSnOt6pf6wMjNXc3QAAwEAAwIAA20AA_rBAQABHwQ",
            "file_unique_id": "AQADMjNXc3QAA_rBAQAB",
            "file_size": 10156,
            "width": 320,
            "height": 178
          },
          {
            "file_id": "AgACAgUAAxkBAAIB1mCiz3sYjDHgE7goA5ckC9lRJow7AAISrDEbtQ4YVUGSnOt6pf6wMjNXc3QAAwEAAwIAA3kAA_jBAQABHwQ",
            "file_unique_id": "AQADMjNXc3QAA_jBAQAB",
            "file_size": 35007,
            "width": 880,
            "height": 491
          },
          {
            "file_id": "AgACAgUAAxkBAAIB1mCiz3sYjDHgE7goA5ckC9lRJow7AAISrDEbtQ4YVUGSnOt6pf6wMjNXc3QAAwEAAwIAA3gAA_vBAQABHwQ",
            "file_unique_id": "AQADMjNXc3QAA_vBAQAB",
            "file_size": 35138,
            "width": 800,
            "height": 446
          }
        ],
        "caption": "kycdocf"
      }
    },
    {
      "update_id": 56245528,
      "message": {
        "message_id": 471,
        "from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "chat": {
          "id": 410894301,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "type": "private"
        },
        "date": 1621282740,
        "forward_from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "forward_date": 1621266757,
        "document": {
          "file_name": "grass.jpg",
          "mime_type": "image/jpeg",
          "thumb": {
            "file_id": "AAMCBQADGQEAAgHXYKLPtLOwnWW6YJ9ZrmXI2rVmrx0AAukBAAK1DhhVva1WI0rXj5119W90dAADAQAHbQADHxIAAh8E",
            "file_unique_id": "AQADdfVvdHQAAx8SAAI",
            "file_size": 15181,
            "width": 275,
            "height": 183
          },
          "file_id": "BQACAgUAAxkBAAIB12Ciz7SzsJ1lumCfWa5lyNq1Zq8dAALpAQACtQ4YVb2tViNK14-dHwQ",
          "file_unique_id": "AgAD6QEAArUOGFU",
          "file_size": 10290
        }
      }
    }
  ]
}
```

</details>>

- About Bot: <https://api.telegram.org/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/getMe>

```json
{"ok":true,"result":{"id":1893739737,"is_bot":true,"first_name":"KYC via Blockchain","username":"kyconbc_bot","can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false}}
```

- Bot send text message to a user: <https://api.telegram.org/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/sendmessage?chat_id=410894301&text=hello>
  - via `curl`:

  ```sh
  curl -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" -H "Content-Type: application/json" -d @body.json
  ```

  where `body.json` is a file with content:

  ```json
  "chat_id": 24325425425,
  "text": "Hey this is a notification from bot.",
  ```

### File download

- Get the photos the Bot received here: <https://api.telegram.org/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/getupdates>

<details>
<summary><b>Expand: </b></summary>

```json
{
  "ok": true,
  "result": [
    {
      "update_id": 56245607,
      "message": {
        "message_id": 658,
        "from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "chat": {
          "id": 410894301,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "type": "private"
        },
        "date": 1621371902,
        "forward_from": {
          "id": 410894301,
          "is_bot": false,
          "first_name": "abhi3700",
          "last_name": "• EOSIO",
          "username": "abhi3700",
          "language_code": "en"
        },
        "forward_date": 1621371821,
        "photo": [
          {
            "file_id": "AgACAgUAAxkBAAICkmCkK_7IbV8esuN4vYTT1jToIuJoAAIsrDEbHBYhVbYvqKYWFMRnnMwlbXQAAwEAAwIAA20AA9vlBQABHwQ",
            "file_unique_id": "AQADnMwlbXQAA9vlBQAB",
            "file_size": 3892,
            "width": 320,
            "height": 223
          },
          {
            "file_id": "AgACAgUAAxkBAAICkmCkK_7IbV8esuN4vYTT1jToIuJoAAIsrDEbHBYhVbYvqKYWFMRnnMwlbXQAAwEAAwIAA3gAA9zlBQABHwQ",
            "file_unique_id": "AQADnMwlbXQAA9zlBQAB",
            "file_size": 10641,
            "width": 800,
            "height": 557
          },
          {
            "file_id": "AgACAgUAAxkBAAICkmCkK_7IbV8esuN4vYTT1jToIuJoAAIsrDEbHBYhVbYvqKYWFMRnnMwlbXQAAwEAAwIAA3kAA93lBQABHwQ",
            "file_unique_id": "AQADnMwlbXQAA93lBQAB",
            "file_size": 18516,
            "width": 1280,
            "height": 891
          }
        ],
        "caption": "kycdocf"
      }
    }
  ]
}
```

</details>

- Get the `file_path` from `file_id` by selecting `small_file_id`: <https://api.telegram.org/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/getfile?file_id=AgACAgUAAxkBAAICkmCkK_7IbV8esuN4vYTT1jToIuJoAAIsrDEbHBYhVbYvqKYWFMRnnMwlbXQAAwEAAwIAA20AA9vlBQABHwQ>

```json
{
  "ok": true,
  "result": {
    "file_id": "AgACAgUAAxkBAAICkmCkK_7IbV8esuN4vYTT1jToIuJoAAIsrDEbHBYhVbYvqKYWFMRnnMwlbXQAAwEAAwIAA20AA9vlBQABHwQ",
    "file_unique_id": "AQADnMwlbXQAA9vlBQAB",
    "file_size": 3892,
    "file_path": "photos/file_1.jpg"
  }
}
```

- Now, Download the file like this: <https://api.telegram.org/file/bot1893739737:AAGAVoUXZ-OB27iYvy9HyyvErtkoDbqB1RA/profile_photos/file_1.jpg> For more, refer [here](https://core.telegram.org/bots/api#getfile)
