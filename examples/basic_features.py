from skateboard import Skateboard
from skateboard.objects import SkateboardDivider, SkateboardParagraph

sb = Skateboard()
sb.add_object(SkateboardDivider(id="hello_world"))
sb.add_object(SkateboardDivider())
sb.add_object(SkateboardDivider())
sb.add_object(SkateboardParagraph("Hello"))


sb.start()