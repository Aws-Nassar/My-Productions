CC = g++
CFLAGS =
DEPS =
OBJ = apply_filter.o papply_filter.o

%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

apply_filter: apply_filter.o
	$(CC) -o $@ $^ $(CFLAGS)

papply_filter: papply_filter.o
	$(CC) -o $@ $^ $(CFLAGS)

test1: apply_filter papply_filter
	./apply_filter oimage.txt EdgeMask.txt nimageSerial.txt
	./papply_filter oimage.txt EdgeMask.txt nimageParallel.txt 3

clean:
	rm -f *.o *~ apply_filter papply_filter
