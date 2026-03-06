1) Discuss how the two approaches address measurement issues and when to use each.

When timing a program, measurements can be affected by timer resolution limits, CPU scheduling, background processes, cache effects, and garbage collection. These sources of noise can make a single timing unreliable.

timeit.timeit(..., number=N) runs the function many times in a single loop and returns the total execution time. This reduces small measurement errors and timer inaccuracy by making the total runtime longer and averaging out tiny fluctuations. It is most appropriate when the function runs very quickly and a single execution would be too short to measure accurately.

timeit.repeat(..., repeat=R, number=N) runs the timed block multiple separate times and returns a list of total times. This helps account for run-to-run variation caused by system-level interference (e.g., background processes). It is appropriate when you want a more reliable estimate and need to observe variability between runs

2) Which statistic is appropriate for each, and why?

For timeit.timeit(), the appropriate statistic is the average time per run, computed as total_time / number. Since it returns only one total time for multiple executions, dividing by number gives the best estimate of the typical execution time.

For timeit.repeat(), the appropriate statistic is the minimum of the returned times. This is because external noise and system interruptions usually make runs slower, not faster. The minimum time is therefore the closest estimate of the true execution time without interference.