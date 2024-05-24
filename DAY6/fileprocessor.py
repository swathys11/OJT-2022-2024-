class FileProcessor:
    @staticmethod
    def read_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."

    @staticmethod
    def write_file(file_name, data):
        try:
            with open(file_name, 'w') as file:
                file.write(data)
                return "Data written successfully."
        except Exception as e:
            return f"Error writing data: {str(e)}"

    @staticmethod
    def append_file(file_name, data):
        try:
            with open(file_name, 'a') as file:
                file.write(data)
                return "Data appended successfully."
        except Exception as e:
            return f"Error appending data: {str(e)}"


file_name = "example.txt"
print(FileProcessor.write_file(file_name, "Hello, World!\nThis is a test."))
print(FileProcessor.read_file(file_name))
print(FileProcessor.append_file(file_name, "\nAppending more data."))
print(FileProcessor.read_file(file_name))
