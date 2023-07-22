import tkinter as tk
from tkinter import filedialog

# Size of Tkinter root window
window_size: tuple[int, int] = (500, 200)
# Name to save output file as
save_file_name: str = "text_output.txt"

def main() -> None:
    """Entry point of text editor application"""
    # Create window
    window: tk.Tk = tk.Tk()
    window.title("Our Text Editor!")
    window.geometry(f"{window_size[0]}x{window_size[1]}")

    # Create text editor Text widget
    text_editor: tk.Text = tk.Text(master=window, height=10)
    text_editor.pack()

    # Create save button widget
    save_button: tk.Button = tk.Button(master=window, text="Save", command=lambda: save_text_callback(text_editor=text_editor))
    save_button.pack()

    # Start the Tkinter loop
    tk.mainloop()

def save_text_callback(text_editor: tk.Text) -> None:
    """
    Saves text widget's text to .txt file of user's
    chosen path.
    """
    # Get text to write to file and get path of file
    text: str = text_editor.get(0.1, tk.END)
    save_path: str = filedialog.askdirectory(initialdir=".", title="Save to")

    # Output text to file
    with open(f"{save_path}/{save_file_name}", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()