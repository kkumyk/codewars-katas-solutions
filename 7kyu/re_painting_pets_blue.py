# grey dog   => blue dog

import re

search = ".+(?= (dog|cat))"
substitute = "blue"

str = "grey dog"
new_str = re.sub(r".+(?= (dog|cat))", "blue", str)

print(new_str)
