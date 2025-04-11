# Telegram-Bot Rust

## Description

There is a teloxide crate for Rust which is used to create Telegram bots.

## Notes

### Async

**Q. Is there any benefit of running a telegram bot in multi-threaded setup?**

```rust
#[tokio::main]
async fn main() {
  // ...
}
```

**A.** Teloxide handles updates from different chats concurrently by default, so you definitely will get some benefits from multi-thread runtime/executor.

> DISCLAIMER: It is to be kept in mind that `Arc` does increase (lowest among all the shared pointers) the runtime overhead of the code. It has been found though that messages are getting deleted faster (concurrently/parallely) when using `Arc` in the code.

Example added in [subspace-telegram-bot](https://github.com/abhi3700/subspace-telegram-bot) in [commit - 3997b223](https://github.com/abhi3700/subspace-telegram-bot/commit/3997b2236b029cbbb0c3dea6e8f138128f674686). Although this example has 2 messages deleted. But, the actual use case would be in managing group messages. Here, 2 API calls being made concurrently.

> Actually, `teloxide` doesn't support the [`deleteMessages` API endpoint](https://core.telegram.org/bots/api#deletemessages) as of `13-Feb-2024`. So, the only way to delete messages is to use the `deleteMessage` API endpoint. This means that we can't delete multiple messages at once. We have to delete them one by one. This is where `Arc` comes into play. We can use `Arc` to share the same message across multiple threads and delete them concurrently.

### User

User related details.

- Get username of a user from `Message` type:

```rust
pub(crate) async fn operator_command(bot: Bot, msg: Message) -> HandlerResult {
 bot.send_message(msg.chat.id, format!("Your username is {}", msg.from.unwrap().id.0))
    .await?;

 Ok(())
}
```

- Get user id from `Message` type in private/group chats:

```rust
pub(crate) async fn tg_uid(bot: Bot, msg: Message) -> HandlerResult {
  let uid = msg.chat.id.0; // [RECOMMENDED for personal chats]
  // let uid = msg.from().unwrap().id.0; [used in group chats as the last message sent by whoever]
 bot.send_message(msg.chat.id, format!("Your username is {}", msg.from().unwrap().id.0))
    .await?;

 Ok(())
}
```

### Chat, Message

- <u>Message</u>: When a user sends a message to the bot, a `Message` type is sent. This means that we can have a function that takes argument-type param like this:

```rust
pub(crate) async fn balance_command(
    bot: Bot,
    dialogue: MyDialogue,
    msg: Message,
    text: String,
) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    // ...

    Ok(())
}
```

  Here, if a message is sent (from App to bot) like `"/balance 0xabc"`, then `msg = "/balance 0xabc"` & `text = "0xabc"`.

### Keyboard

#### Inline

- <u>CallbackQuery</u>: When a user clicks on a button, a `CallbackQuery` (provided it is defined like `InlineKeyboardButton::callback(...)`) type is sent. This means that we can have a function that takes this type like this:

```rust
pub(crate) async fn balance_callback(
    bot: Bot,
    dialogue: MyDialogue,
    q: CallbackQuery,
) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    // ...
    let text = q.data;

    bot.send_message(dialogue.chat_id(), format!("You clicked on {}", text))
            .parse_mode(ParseMode::MarkdownV2)
            .await?

    Ok(())
}
```

- <u>Url</u>: For a url attached to a button, a `url` field is used in `InlineKeyboardButton` type. This means that we can have a function that takes this type like this:

```rust
pub(crate) fn kb_operator() -> InlineKeyboardMarkup {
 InlineKeyboardMarkup::new(vec![
  vec![
   InlineKeyboardButton::url(
    "Task-1",
    Url::from_str("https://example.com")
     .unwrap_or_else(|_| panic!("Invalid url")),
   ),
   InlineKeyboardButton::url(
    "Task-2",
    Url::from_str("https://example.com")
     .unwrap_or_else(|_| panic!("Invalid url")),
   ),
  ],
  vec![
   InlineKeyboardButton::url(
    "Task-3",
    Url::from_str("https://example.com")
     .unwrap_or_else(|_| panic!("Invalid url")),
   ),
   InlineKeyboardButton::url(
    "Task-4",
    Url::from_str("https://example.com")
     .unwrap_or_else(|_| panic!("Invalid url")),
   ),
  ],
 ])
}


pub(crate) async fn select_command(bot: Bot, msg: Message) -> HandlerResult {
 send_md_msg_kb!(bot, msg, "Select one:", kb_operator());

 Ok(())
}
```

#### Reply

- `KeyboardMarkup` (formerly `ReplyKeyboardMarkup`) is used to create a keyboard with buttons. It is used in `send_message` method of `Bot` type.
- Each button is created using `KeyboardButton` type.

```rust
/// UI for /faq
pub(crate) fn kb_test() -> KeyboardMarkup {
    let buttons = [
      ("Q1", "https://subspace.network/"),
      ("Q2", "https://subspace.network/"),
      ("Q3", "https://subspace.network/"),
      ("Q4", "https://subspace.network/"),
      ("Q5", "https://subspace.network/"),
      ("Q6", "https://subspace.network/"),
    ];
    let mut keyboard: Vec<Vec<KeyboardButton>> = vec![];

    // each row has a maximum of $max_buttons_per_row buttons
    for row in buttons.chunks(2) {
      let buttons_row: Vec<KeyboardButton> = row
      .iter()
      .map(|&(text, url)| KeyboardButton {
        text: text.to_string(),
        request: Some(ButtonRequest::WebApp(WebAppInfo {
        url: Url::from_str(url).unwrap(),
        })),
      })
      .collect();
      keyboard.push(buttons_row);
    }

    KeyboardMarkup::new(keyboard).resize_keyboard(true).one_time_keyboard(true)
}
```

### Dialogue, Storage

- <u>Without storage</u>: In case of dialogue, if you follow the teloxide [`purchase.rs`](https://github.com/teloxide/teloxide/blob/2945f4d30137ad65e94d08516967617cca86ff6a/crates/teloxide/examples/purchase.rs) example, then you will find that `/start` command triggers dialogue where in `Commands` enum, `Start` variant is used. This means that when a user sends `/start` command, then `Start` variant is triggered & the dialogue starts.

  But, imagine a case where `/start <abc>` needs to trigger dialogue. In this case, we can use `Start(String)` variant in `Commands` enum. This means that when a user sends `/start <abc>`, then `Start(String)` variant is triggered & the dialogue starts. Look at /balance command of [Example](https://github.com/abhi3700/subspace-telegram-bot). Here, in the `BalanceState` enum, we don't need any Balance variant, we can just start from `ReceiveChainChoice`. [Code](https://github.com/abhi3700/subspace-telegram-bot/blob/8af4e100d712f88b6ee68f2681926b87a1714a12/src/handlers/balance.rs#L24-L126)

- <u>With Storage</u>: In a flow, if you are taking number based input vs string based input, then you need to add an additional state in the latter. Shown below are 2 examples where in the Eg-1, number is taken as input & in the Eg-2, string is taken as input.

  - Eg-1: Number based input

  ```rust
  pub enum MyDialogueState {
      Start,  // Please send your number
      End(i32), // Your number is {}
  }
  ```

  - Eg-2: String based input

  ```rust
  pub enum MyDialogueState {
      Start, // Please send your name
      ReceiveName(String), 
      End,
  }
  ```

  > NOTE: The value is stored on a per-user basis (i.e. Alice has the same data stored if not changed with the bot, even after the bot is deleted & restarted chat conversation) irrespective of whether the bot is stopped (next time it will have the data persistence) or still running.<br/>
  But, in order to have a data persistence across multiple users' (Alice, Bob, Charlie, etc.) sessions with the same bot, you need a global database.

  > Cons: Here, once the storage state is set like `Start`, `ReceiveName`, then it is not possible to change the name. This can be renamed only after deleting the bot or may be try with revoking the current API key with a new one.

- If we have 2 dialogue states for multiple commands (/foo, /bar), then we have to club them into global state for the dialogue. It is done in this example: [subspace-telegram-bot](https://github.com/abhi3700/subspace-telegram-bot), view commit changes in [PR #3](https://github.com/abhi3700/subspace-telegram-bot/pull/3/commits/33762c7fdd9477821d98c73086ede68c18a1aefe) of the repo.
- Suppose, you have to accept title, desc, photos. Then, the dialogue state become like this:

```rust
pub(crate) enum SupportIssueState {
  #[default]
  ReceiveTitle,
  ReceiveDesc {
    title: String,
    tries: u8,
  },
  ReceivePhotos {
    title: String,
    desc: String,
  },
  ReceiveOtpConfirmation {
    title: String,
    desc: String,
    photos: Vec<String>,
    tries: u8,
  },
}
```

And the function for receive desc is like this:

```rust

pub(crate) async fn issue_receive_desc(
  bot: Bot,
  dialogue: GlobalDialogue,
  // Available from `SupportIssueState::ReceiveDesc {title, tries}`
  (title, tries): (String, u8),
  msg: Message,
  ) -> HandlerResult<()> {
  ..
```

> NOTE: Here, the previous arguments to be saved in dialogue are in tuples.

## References

### Libs

- [teloxide](https://github.com/teloxide/teloxide)
  - <https://github.com/LasterAlex/teloxide_tests>
    - <https://github.com/LasterAlex/teloxide_tests/tree/master/examples>
      - Album bot
      - ..
- [tgbot: A full-featured Telegram Bot API client](https://github.com/tg-rs/tgbot)
- [⚡rustygram is a minimal and blazing fast telegram notification framework for Rust](https://github.com/ExtremelySunnyYK/rustygram)
- [telers]<https://github.com/Desiders/telers> supports till latest Telegram Bot API (7.2 atm).

### Bots

- [Search CJK messages of supergroups in Telegram](https://github.com/krishukr/telegram-cjk-search-bot)
- [An RSS/Atom bot for telegram channels](https://github.com/rossnomann/telefeed)
- [A Telegram ChatGPT bot written in Rust](https://github.com/flows-network/telegram-gpt)

For more, click [here](https://github.com/topics/telegram-bot?l=rust&o=desc&s=updated)

### Blogs

- [Migrating my family finance bot from Python to Rust (teloxide) because I am tired of exceptions (part 1)](https://trkohler.com/posts/i-migrated-my-family-finance-bot-from-python-to-rust-because-i-am-tired-of-exceptions/)
- [Migrating my family finance bot from Python to Rust (teloxide) [part 2]](https://trkohler.com/posts/migrating-my-family-finance-bot-from-python-to-rust-teloxide-part-2/)
