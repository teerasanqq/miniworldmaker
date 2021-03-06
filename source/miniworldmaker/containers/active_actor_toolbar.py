from miniworldmaker.containers.toolbar import Toolbar
from miniworldmaker.containers.toolbar_widgets import *
from miniworldmaker.tokens import actor as act

class ActiveActorToolbar(Toolbar):

    def __init__(self):
        super().__init__()
        self.position = "right"
        self.actor = None
        self.register_events.add("all")


    def _add_to_window(self, window, dock, size=None):
        super()._add_to_window(window, dock, size)
        for actor in self.window.board.tokens:
          #if self.actor.__class__ == act.Actor:
          self.add_widget(ActorButton(text=actor.__class__.__name__, actor=actor, toolbar = self))

    def get_event(self, event, data):
        super().get_event(event, data)
        if event == "active_token":
            self.actor = data
        if self.actor is not None:
            if event == "active_token" or event == "actor_moved":
                self.actor = data
                self.remove_all_widgets()
                self.add_widget(ToolbarLabel("ID:" + str(self.actor.token_id)))
                self.add_widget(ToolbarLabel("Direction:" + str(self.actor.direction)))
                self.add_widget(ToolbarLabel("Position:" + str(self.actor.position)))
                self.add_widget(ToolbarLabel("Is at Border:" + str(self.actor.is_at_border())))
                self.add_widget(ToolbarLabel("Is on Board:" + str(self.actor.is_on_the_board())))
                method_list = [func for func in self.actor.__class__.__dict__ if not func.startswith("_") and not func in 'get_event']
                for method in method_list:
                    self.add_widget(MethodButton(text="--> call method: {0}".format(method), actor=self.actor, method = method))
        else:
            for actor in self.window.board.tokens:
                if self.actor.__class__ == act.Actor:
                    self.add_widget(ActorButton(text=self.actor.__class__.name, actor=actor))

class MethodButton(ToolbarButton):

    def __init__(self, text, actor, method ):
        super().__init__(text=text)
        self.actor = actor
        self.method = method

    def get_event(self, event, data):
        if self.actor is not None:
            getattr(self.actor, str(self.method))()

class ActorButton(ToolbarButton):

    def __init__(self, text, actor, toolbar):
        super().__init__(text=text)
        self.actor = actor
        self.toolbar = toolbar

    def get_event(self, event, data):
        if not  self.toolbar.window.board.active_actor == self.actor:
            self.toolbar.window.board.set_active_actor(token = self.actor)
            self.actor.costume.show_info_overlay()
