from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, RichLog
from textual.containers import Horizontal
from textual.binding import Binding
from agent import ask_agent
import threading

class ResearchApp(App):
    BINDINGS=[
        Binding("ctrl+q","quit","Quit"),
        Binding("ctrl+l","clear_log","Clear"),
        Binding("ctrl+k","clear_chat","Reset"),
    ]
    def compose(self)->ComposeResult:
        yield Header()
        self.chat=RichLog()
        self.tools=RichLog()
        yield Horizontal(self.chat,self.tools)
        yield Input(placeholder="Ask research question...")
        yield Footer()

    def action_clear_log(self): self.tools.clear()
    def action_clear_chat(self): self.chat.clear()

    def on_input_submitted(self,event):
        q=event.value
        event.input.value=""
        self.chat.write(f"You: {q}")
        threading.Thread(target=self.run_agent,args=(q,),daemon=True).start()

    def run_agent(self,q):
        self.tools.write("Running agent...")
        ans=ask_agent(q, self.tools.write)
        self.chat.write(f"Bot: {ans}")

if __name__=="__main__":
    ResearchApp().run()
