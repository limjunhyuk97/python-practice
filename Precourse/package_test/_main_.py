# import package.module
import unit.character

unit.character.test()

# from package import module
from unit import item
item.test()

# from package import *
# __init__ module 내에 import 가능한 대상 module들을 "from . import (module1), (module2), ,,," 형식으로 적어주어야 한다.
from unit import *
character.test()

# import package
import unit
unit.item.test()
unit.character.test()
unit.monster.test()