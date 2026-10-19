const { Client, GatewayIntentBits, REST, Routes, SlashCommandBuilder } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

const DISCORD_TOKEN = process.env.DISCORD_TOKEN; // Nhớ add TOKEN trong Render Environment!
const CLIENT_ID = "1560837328220721362";

const commands = [
  new SlashCommandBuilder()
    .setName('ff')
    .setDescription('Lệnh Free Fire của Sen')
    .toJSON()
];

const rest = new REST({ version: '10' }).setToken(TOKEN);

client.once('ready', async () => {
  console.log(`Logged in as ${client.user.tag}!`);
  try {
    await rest.put(Routes.applicationCommands(CLIENT_ID), { body: commands });
    console.log('Đã sync lệnh /ff thành công!');
  } catch (err) {
    console.error(err);
  }
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;
  if (interaction.commandName === 'ff') {
    await interaction.reply('🔥 Bot Free Fire của Sen đang hoạt động! YEAHHH!');
  }
});

client.login(DISCORD_TOKEN);