def purify(items):
     for item in items:
          if item % 2 != 0:
               items.remove(item);
               purify(items);
     return items;
     
print purify([1,2,3,])

