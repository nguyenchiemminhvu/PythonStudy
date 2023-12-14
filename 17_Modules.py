import sys
before_import = set(sys.modules.items())
import sub_modules.converter
after_import = set(sys.modules.items())
print("Which module is just imported? ->", after_import - before_import)

nums = [1,2,3,4,5]
output = sub_modules.converter.collection_to_string(nums)
print(output)
