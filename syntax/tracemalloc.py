# слежка за утеской памяти
import tracemalloc 
 
tracemalloc.start() 
 
# Код, который может вызывать утечку 
data = [x for x in range(10_000)] 
 
snapshot = tracemalloc.take_snapshot() 
top_stats = snapshot.statistics('lineno') 
 
for stat in top_stats[:3]:  # Топ-3 "подозреваемых" 
    print(f"{stat.count} блоков: {stat.size / 1024} КБ") 
    print(stat.traceback.format()[-1])  # Где выделена память 