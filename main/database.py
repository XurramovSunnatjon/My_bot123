import aiosqlite

class Database:
    def __init__(self, db_file):
        self.db_file = db_file

    async def create_tables(self):
        async with aiosqlite.connect(self.db_file) as db:
            # Foydalanuvchilar jadvali
            await db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)")
            # Kanallar jadvali
            await db.execute("CREATE TABLE IF NOT EXISTS channels (channel_id TEXT PRIMARY KEY, url TEXT)")
            await db.commit()

    async def add_user(self, user_id):
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
            await db.commit()

    async def add_channel(self, channel_id, url):
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute("INSERT OR REPLACE INTO channels (channel_id, url) VALUES (?, ?)", (channel_id, url))
            await db.commit()

    async def get_channels(self):
        async with aiosqlite.connect(self.db_file) as db:
            async with db.execute("SELECT channel_id, url FROM channels") as cursor:
                return await cursor.fetchall()

