# DCNewPostBot
## English
### What does it do?  
This is a Discord bot that scrapes posts on a specific DCInside gallery and links new ones to a Discord channel.

### How do I set it up?  
These instructions assume a UNIX-like environment (macOS, Linux, etc)

#### 0. External dependencies:
- `discord.py`: `pip3 install discord`
- `dc_api`: `pip3 install dc_api`
- `filetype`: `pip3 install filetype`

#### 1. Clone the repository, and navigate into it.
```shell
git clone https://github.com/goonmandu/DCNewPostBot.git
cd DCNewPostBot
```

#### 2. Make a Discord bot with the following permissions:  
*Permissions in italics* may not be necessary, but are untested.


- General Permissions:
  - *none*


- Text Permissions:
  - Send messages
  - *Manage messages*
  - Embed links
  - *Read message history*


- Voice Permissions:
  - *none*


#### 3. Copy your bot token.

#### 4. Create `bot_token.py` in the root directory of the repository, and structure it like so:
```py
BOT_TOKEN = "your bot token goes here"
```

#### 5. Invite the bot to your server.

#### 6. Edit the bot settings in `bot_constants.py` to suit your needs.

#### 7. Launch the bot:
```shell
python3 bot.py
```

#### 7-1. To start the Python process "detached" from the terminal window (keep it alive even when you close the terminal or `ssh` session):
```shell
nohup python3 bot.py &
```

#### 7-2. To stop the bot process started with 7-1:
```shell
ps aux | grep -i "python3 bot.py &"  # Check PID
kill -2 <The PID from above command>
```

## 한국어
### 뭐 하는 봇이예요?
디시인사이드 갤러리에 새로 올라오는 글을 스크레이핑해서 디스코드 채널에 링크해주는 디스코드 봇입니다.

### 직접 써보고 싶어요.  
이 가이드는 UNIX 계열의 운영 체제(macOS, Linux 등)를 기반으로 작성되었습니다.

#### 0. 외부 의존 패키지를 설치하세요.
- `discord.py`: `pip3 install discord`
- `dc_api`: `pip3 install dc_api`
- `filetype`: `pip3 install filetype`

#### 1. 이 리포지토리를 클론하고, 생성된 폴더로 진입하세요.
```shell
git clone https://github.com/goonmandu/DCNewPostBot.git
cd DCNewPostBot
```

#### 2. 아래 권한을 가진 디스코드 봇 계정을 만드세요.
*이탤릭체 된 권한*은 필요 없을지도 있지만, 확인되지는 않았습니다.


- General Permissions:
  - *없음*


- Text Permissions:
  - Send messages
  - *Manage messages*
  - Embed links
  - *Read message history*


- Voice Permissions:
  - *없음*


#### 3. 봇 토큰을 복사하세요.

#### 4. 리포지토리 폴더 안에 `bot_token.py` 파일을 만들고, 아래의 양식대로 작성하세요.
```py
BOT_TOKEN = "복사한 봇 토큰을 여기에 붙여넣기하세요"
```

#### 5. 봇을 사용하고 싶은 서버에 초대하세요.

#### 6. 필요한 대로 `bot_constants.py`를 편집해서 봇을 설정하세요.

#### 7. 봇을 실행하세요.
```shell
python3 bot.py
```

#### 7-1. 터미널 창이나 `ssh` 연결이 끊어져도 Python 프로세스가 실행되도록 남기고 싶다면, 아래 명령어로 실행하세요.
```shell
nohup python3 bot.py &
```

#### 7-2. (7-1)의 명령어로 실행한 봇을 멈출 때는 이렇게 하세요.
```shell
ps aux | grep -i "python3 bot.py &"  # PID 확인
kill -2 <위 명령에서 확인한 PID>
```