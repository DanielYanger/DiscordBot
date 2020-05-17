const Discord = require("discord.js");
const bot = new Discord.Client();

//implementing login

const token = "NzExMzg5Nzc1ODQ4MDEzODQ1.XsCThQ.GJUizIy7udNcx1ZvlXoJhjxoCbg";

bot.on("ready", () => {
  console.log("Bot is online!");
});

bot.on("message", (msg) => {
  if (msg.content === "Hello") {
    msg.reply("Hi");
  }
});

bot.login(token);
