
# PY [ 📝 ] File

# 1 Libraries
import os
import shutil
import csv
import json
from rich.console import Console

# 2 Configuration
console = Console()

# PY How To Create New File Or Replace Content [W]

with open("Design/js/script.js", "w", encoding="utf-8") as file:
    file.write("console.log(`Hello, This Is a New Content!`);")

with open("Design/css/style.css", "w", encoding="utf-8") as file:
    file.write("""
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 95vh;
  height: 96vh;
  background-color: #4437ff;
}
""")

console.print("✅ File Created Successfully [W]!", style="bold green")
console.print("_" * 90, style="bold green")

# PY How To Create a New  File [X]
try:
    with open("Design/index.html", "x", encoding="utf-8") as file:
        file.write("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>My Page</title><link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <h1>Welcome to My Page</h1><script src="js/script.js"></script>
  </body>
</html>
""")
        console.print("✅ File Created Successfully [X]!", style="bold green")
        console.print("_" * 90, style="bold green")
except FileExistsError:
    console.print("❌ File Already Exists [X]!", style="bold red")
    console.print("_" * 90, style="bold red")

# PY How To Adding New Content [A]
with open("Design/css/style.css", "a", encoding="utf-8") as file:
    file.write("""
h1 {
  color: #fff;
}
""")

console.print("🖊️  File Adding Successfully [A]!", style="bold green")
console.print("_" * 90, style="bold green")

# PY How To Read The Entire File [R]
with open("Design/css/style.css", "r", encoding="utf-8") as file:
    content = file.read()
    console.print("📜 File Read Successfully [R]!", style="bold green")
    console.print(f"{content}", style="bold yellow")
    console.print("_" * 90, style="bold yellow")

# PY How To Check If a File or Folder Exists [If Else]

if os.path.exists("Design/css/scss/File_will_delete.scss"):
    console.print("✅ The File Exists!", style="bold green")
    console.print("_" * 90, style="bold green")
else:
    console.print("❌ The File Does Not Exist.", style="bold red")
    console.print("_" * 90, style="bold red")

if os.path.isfile("Design/css/scss/File_will_delete.scss"):
    console.print("📝 It's a File!", style="bold yellow")
    console.print("_" * 90, style="bold yellow")
elif os.path.isdir("Design/css/scss/File_will_delete.scss"):
    console.print("📂 It's a Directory!", style="bold yellow")
    console.print("_" * 90, style="bold yellow")

# PY How To Delete File | Empty Folder | Folder With Files [Delete]

if os.path.exists("Design/css/scss/File_will_delete.scss"):
    os.remove("Design/css/scss/File_will_delete.scss")
    console.print("🗑️  File deleted successfully!", style="bold green")
    console.print("_" * 90, style="bold green")
else:
    console.print("❌ File does not exist!", style="bold red")
    console.print("_" * 90, style="bold red")

if os.path.exists("Design/css/scss"):
    os.rmdir("Design/css/scss")
    console.print("🗑️  Folder Deleted!", style="bold yellow")
    console.print("_" * 90, style="bold yellow")
else:
    console.print("❌ The Folder Does Not Exist.", style="bold red")
    console.print("_" * 90, style="bold red")

if os.path.exists("Design/css/Framework"):
    shutil.rmtree("Design/css/Framework")
    console.print("🗑️  Folder And Its Contents Delete!", style="bold yellow")
    console.print("_" * 90, style="bold yellow")
else:
    console.print("❌ The Folder Does Not Exist.", style="bold red")
    console.print("_" * 90, style="bold red")

# PY How To Rename Files [Rename]

# old_file_path = "F:/Python_File_Operations/Design/css/oldname.css"
# new_file_path = "F:/Python_File_Operation/Design/css/newname.css"
old_file_path = "Design/css/oldname.css"
new_file_path = "Design/css/newname.css"
if os.path.exists("Design/css/oldname.css"):
    os.rename(old_file_path, new_file_path)
    # os.rename("oldname.css", "newname.css")
    console.print("✍️  File renamed successfully!", style="bold green")
    console.print("_" * 90, style="bold green")
else:
    console.print("❌ The file 'oldname.txt' does not exist.", style="bold red")
    console.print("_" * 90, style="bold red")

# PY How To Write Or Read Data to CSV File

with open("Design/Data/data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Jane", 35, "London"])
    writer.writerow(["John", 40, "New York"])

with open("Design/Data/data.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        console.print("📦  File CSV successfully!", style="bold green")
        console.print(f"{row}", style="bold blue")
        console.print("_" * 90, style="bold blue")

# PY How To Write Or Read Data To JSON File

data = {"name": "John", "age": 30, "city": "New York"}
with open("Design/Data/data.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)

with open("Design/Data/data.json", "r", encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)
    console.print("📦  File JSON successfully!", style="bold green")
    console.print(f"{data}", style="bold yellow")
    console.print("_" * 90, style="bold yellow")

# PY How To Copy File

shutil.copy("Design/Data/data.json", "Design/Data/destination.json")
console.print("📝  File Copy successfully!", style="bold yellow")
console.print("_" * 90, style="bold yellow")

# PY How To Transfer File [Move]

shutil.move("Design/Data/destination.json", "Design/js/destination.json")
console.print("📝  File Move successfully!", style="bold green")
console.print("_" * 90, style="bold green")
