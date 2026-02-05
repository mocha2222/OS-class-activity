import java.util.concurrent.*;

public class ExecutorExample {

    public static void main(String[] args) throws InterruptedException {

        // Single Thread Executor
        ExecutorService single = Executors.newSingleThreadExecutor();
        single.execute(() -> System.out.println("Single Thread Executor"));
        single.shutdown();

        // Cached Thread Pool
        ExecutorService cached = Executors.newCachedThreadPool();
        for (int i = 1; i <= 3; i++) {
            int id = i;
            cached.execute(() -> {
                System.out.println("Cached Thread " + id);
            });
        }
        cached.shutdown();

        // Fork-Join Pool
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        forkJoinPool.submit(() ->
            forkJoinPool.submit(() ->
                System.out.println("Fork-Join Parallel Task"))
        );

        forkJoinPool.shutdown();
    }
}
