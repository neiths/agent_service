## Getting Started

To get started with this project, you need to configure your environment variables. Follow the steps below to set up your environment:

### 1. Copy `.env.example` to `.env`

First, you need to create a `.env` file based on the `.env.example` file. This file contains all the necessary environment variables for the project. Run the following command in your terminal:

```sh
# linux
cp .env.example .env
```

### 2. Set Up a Python Virtual Environment

Next, create and activate a Python virtual environment to isolate your project dependencies.

```python
# create a python environment
python -m venv venv

# activate
venv/Scripts/activate (windows)
source venv/Scripts/activate (linux)
```

### 3. Install Project Dependencies

With the virtual environment activated, install the necessary dependencies using pip:

```python
# Install dependencies
pip install -r requirements.txt
```

### 4. Configure the Database

Run the following commands to create and apply the database migrations:

```python
# Run database migrations
python manage.py makemigrations
python manage.py migrate
```

```bash
# https://github.com/pgvector/pgvector
# make sure add pgvector into postgres.
# if psql installed.
psql -U yourusername -d yourdatabase -c "CREATE EXTENSION vector;"

# if you have some trouble about makemigrations or migrate.
# Do it when you have no idea how to fix the errors. (Not recommended)
psql -U yourusername -d yourdatabase -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
```

### 5. Start the Development Server

Finally, start the development server to run your application:

```python
python manage.py runserver
```

### 6. Create super user

```python
python manage.py createsuperuser
```

## API Endpoints

Here are the API endpoints available in this project:

### Admin Panel

- **Manage Database:** `http://127.0.0.1:8000/admin/`
  - Access the Django admin panel to manage the database and other admin tasks.

### System Prompt Management

- **Manage System Prompts:** `http://127.0.0.1:8000/system-prompt/`
  - Endpoint to manage system prompts.
  - **Get a Single System Prompt:** `http://127.0.0.1:8000/system-prompt/{id}/`
    - Replace `{id}` with the ID of the specific system prompt.
  - **Post a System Prompt:**
    - Send a POST request with the following JSON structure:
    ```json
    {
      "prompt_name": "",
      "prompt_content": ""
    }
    ---
    ```

### External Knowledge ( Database )

- ** User Database:** `http://127.0.0.1:8000/admin/core_app/externalknowledge/`
  - Endpoint to User Database.
  - **Post an External Knowledge:**
    - Send a POST request with the following JSON structure:
    ```json
    {
      "subject": "",
      "chapter": "",
      "content": ""
    }
    ```

### Agent tools

- **Mange Agent Tools:** `http://127.0.0.1:8000/admin/core_app/agenttool/`
  - Endpoint to Agent Tools.
  - **Post Agent tools:**
  - Send a POST request with the following JSON structure:
  ```json
  {
    "tool_name": "",
    "args_schema": [
       {}
    ],
    "description": ""
  }
  ```

### Agent

- **Mange Agents:** `http://127.0.0.1:8000/admin/core_app/agent/`
- Endpoint to Agents.
- **Post Agents:**
- Send a POST request with the following JSON structure:

  ```json
  {
    "agent_name": "",
    "llm": "",
    "tools": [
       ""
    ],
    "prompt": "" \\id
  }
  ```

### Conversation Management

- **Manage Conversations:** `http://127.0.0.1:8000/conversation/`
  - Endpoint to manage conversations.
  - **Get a Single Conversation:** `http://127.0.0.1:8000/conversation/{id}/`
    - Replace `{id}` with the ID of the specific conversation.
  - **Post Conversation:**
    - Send a POST request with the following JSON structure:
    ```json
    {
      "agent": "", \\id
      "chat_history": [] \\[{"", ""}]
    }
    ```

### Answer Mangement

- **Answer**: `http://127.0.0.1:8000/answer/`
  - Endpoint to manage Answer
  - **Post an Answer:** `http://127.0.0.1:8000/answer/`
  - Send a POST request with the following JSON structure:
    ```json
    {
      "conversation_id": "",
      "message": ""
    }
    ```

### Streaming Mangement

- **Streaming**: `http://127.0.0.1:8000/streaming/`
  - Endpoint to manage Streaming
  - **Post a Streaming:** `http://127.0.0.1:8000/streaming/`
  - Send a POST request with the following JSON structure:
    ```json
    {
      "conversation_id": "",
      "message": ""
    }
    ```

### Flow

Add sysprompt -> Agent tool -> Agent -> Conversation.

Ensure that your server is running before attempting to access these endpoints

## Prompt instructions:

## 1. Cấu Trúc Content

System prompt bao gồm ba phần chính: Ngữ Cảnh, Chức Năng, và Mô Tả Chi Tiết.

### Ngữ Cảnh (Context)

Ngữ cảnh cung cấp bối cảnh tổng quát về mục tiêu và phạm vi của chatbot. Bạn cần mô tả vai trò của chatbot và những gì người dùng có thể mong đợi.

- Ví dụ:

`Bạn là một trợ lý học tập ảo, giúp người dùng tìm kiếm và cung cấp tài liệu học tập từ cơ sở dữ liệu dựa trên embedding của môn học và chương tương ứng.`

### Chức Năng (Functionality)

Chức năng mô tả các hành động chính mà chatbot có thể thực hiện. Bao gồm các công cụ mà chatbot có thể sử dụng.

- Ví dụ:

```
Chức năng của bạn bao gồm:
- Nhận yêu cầu tìm kiếm tài liệu từ người dùng.
- Kiểm tra và xác nhận thông tin về môn học và chương.
- Tìm kiếm thông tin liên quan trong cơ sở dữ liệu.
- Trả lời người dùng với các tài liệu chính xác.
```

### Mô Tả Chi Tiết (Detailed Description)

Mô tả chi tiết cung cấp hướng dẫn cụ thể về cách chatbot xử lý các yêu cầu từ người dùng. Nó nên bao gồm các bước chi tiết để đảm bảo chatbot hoạt động đúng và hiệu quả.

- Ví dụ:

```
1. Nhận yêu cầu từ người dùng:
   - Xác minh rằng yêu cầu có đủ thông tin về môn học và chương.
   - Nếu thiếu thông tin, yêu cầu người dùng cung cấp đầy đủ chi tiết.

2. Xử lý yêu cầu:
   - Truy vấn embedding của môn học và chương từ cơ sở dữ liệu.
   - Sử dụng embedding để tìm kiếm tài liệu tương ứng trong cơ sở dữ liệu.

3. Trả lời người dùng:
   - Cung cấp tài liệu phù hợp với yêu cầu của người dùng.
   - Đảm bảo tài liệu chính xác và đáp ứng đúng nhu cầu.
```

## 2. Hướng Dẫn Khi Kết Hợp Với Tool

Khi sử dụng các công cụ, phần mô tả chi tiết cần bao gồm cách sử dụng các công cụ này trong quá trình xử lý yêu cầu.

- Ví dụ:

Với tool embedding

```
Khi sử dụng embedding tool:
- Lấy embedding của môn học và chương từ cơ sở dữ liệu bằng cách sử dụng lệnh `get_embedding(subject, chapter)`.
- Truy vấn cơ sở dữ liệu bằng cách sử dụng embedding đã lấy để tìm tài liệu phù hợp với lệnh `query_database(embedding)`.

Ví dụ chi tiết:
1.Nhận yêu cầu từ người dùng:
   - "Môn học": Toán
   - "Chương": Đại số

2. Xử lý yêu cầu:
   - Lấy embedding của môn học và chương bằng lệnh: `embedding = get_embedding("Toán", "Đại số")`
   - Truy vấn cơ sở dữ liệu với embedding đã lấy: `documents = query_database(embedding)`

3. Trả lời người dùng:
   - Cung cấp danh sách tài liệu liên quan: `Here are the documents related to Đại số in Toán: [Document List]`
```

Với tool wikipedia

```
Khi sử dụng tool `query_from_wikipedia`:
- Truy vấn Wikipedia với chủ đề cụ thể bằng cách sử dụng lệnh `query_from_wikipedia(topic)`.

Ví dụ chi tiết:
1. Nhận yêu cầu từ người dùng:
   - "Môn học": Lịch sử
   - "Chủ đề": Chiến tranh thế giới thứ hai

2. Xử lý yêu cầu:
   - Sử dụng lệnh `query_from_wikipedia("Chiến tranh thế giới thứ hai")` để truy vấn thông tin trên Wikipedia.

3. Trả lời người dùng:
   - Cung cấp thông tin liên quan đến chủ đề Chiến tranh thế giới thứ hai: `Here is the information related to Chiến tranh thế giới thứ hai: [Extracted Information]`
```
