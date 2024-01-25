# Telegram-Bot Rust

## Description

There is a teloxide crate for Rust which is used to create Telegram bots.

## Notes

- When a user sends a message to the bot, a `Message` type is sent. This means that we can have a function that takes this type like this:

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

Here, if a message is sent like `/balance 0xabc`, then `msg = /balance 0xabc` & `text = 0xabc`.

- When a user clicks on a button, a `CallbackQuery` type is sent. This means that we can have a function that takes this type like this:

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

- In case of dialogue, if you follow the teloxide [`purchase.rs`](https://github.com/teloxide/teloxide/blob/2945f4d30137ad65e94d08516967617cca86ff6a/crates/teloxide/examples/purchase.rs) example, then you will find that `/start` command triggers dialogue where in `Commands` enum, `Start` variant is used. This means that when a user sends `/start` command, then `Start` variant is triggered & the dialogue starts.

  But, imagine a case where `/start <abc>` needs to trigger dialogue. In this case, we can use `Start(String)` variant in `Commands` enum. This means that when a user sends `/start <abc>`, then `Start(String)` variant is triggered & the dialogue starts. Look at /balance command of [Example](https://github.com/abhi3700/subspace-telegram-bot). Here, in the `BalanceState` enum, we don't need any Balance variant, we can just start from `ReceiveChainChoice`. [Code](https://github.com/abhi3700/subspace-telegram-bot/blob/8af4e100d712f88b6ee68f2681926b87a1714a12/src/handlers/balance.rs#L24-L126)
