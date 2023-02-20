import tkinter
import tkinter.ttk
import psutil

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current
cpu_percent = psutil.cpu_percent()

# Get memory information
total_memory = psutil.virtual_memory().total
available_memory = psutil.virtual_memory().available
used_memory = psutil.virtual_memory().used
memory_percent = psutil.virtual_memory().percent

# Get disk information
disk_usage = psutil.disk_usage('/')
total_disk_space = disk_usage.total
used_disk_space = disk_usage.used
free_disk_space = disk_usage.free
disk_percent = disk_usage.percent

# Create a simple GUI window
root = tkinter.Tk()
root.title("내 PC 사양 확인")
root.geometry("700x270+100+100")

lbl = tkinter.Label(root, text="내 PC 사양 !?")
lbl.pack()

treeview = tkinter.ttk.Treeview(
    root, columns=["one", "two"], displaycolumns=["one", "two"])
treeview.pack()

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0", width=100,)
treeview.heading("#0", text="index")

treeview.column("#1", width=250, anchor="center")
treeview.heading("one", text="항목", anchor="center")

treeview.column("#2", width=250, anchor="center")
treeview.heading("two", text="내사양", anchor="center")


# 표에 삽입될 데이터
treelist = [
    ("CPU count", cpu_count),
    ("Bani", cpu_freq),
    ("Boni", f"{cpu_percent}%"),
    ("Total memory", f"{total_memory} bytes"),
    ("Available memory", f"{available_memory} bytes"),
    ("Used memory", f"{used_memory} bytes"),
    ("Memory usage", f"{memory_percent}%"),
    ("Total disk space", f"{total_disk_space} bytes"),
    ("Used disk space", f"{used_disk_space} bytes"),
    ("Free disk space", f"{free_disk_space} bytes"),
    ("Disk usage", f"{disk_percent}%"),
]

# 표에 데이터 삽입
for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")

# GUI 실행
root.mainloop()
