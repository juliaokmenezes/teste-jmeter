import pandas as pd

def new_node_exporter_metrics_df(settings, query_start, query_end, system_version, operation, size):
    # Initialize Prometheus
    p = query.Prometheus(settings.prometheus_url)

    modes = ['iowait', 'softirq', 'steal', 'system', 'user']
    query_results = []

    for mode in modes:
        query_cpu_mode = (
            f"sum by(instance) (irate(node_cpu_seconds_total{{instance='{settings.instance}', job='{settings.job}', mode='{mode}'}}[{settings.query_interval}])) / "
            f"on(instance) group_left sum by (instance)((irate(node_cpu_seconds_total{{instance='{settings.instance}', job='{settings.job}'}}[{settings.query_interval}]))) * 100"
        )

        q_res = p.query_range(query_cpu_mode, query_start, query_end, settings.query_step)
        q_res.columns = [f"cpu_{mode}_usage"]
        query_results.append(q_res)

    query_cpu_total_usage = (
        "cpu_total_usage",
        "(sum by(instance) (irate(node_cpu_seconds_total{instance='" + settings.instance + "', job='" + settings.job + "', mode!='idle'}[" + settings.query_interval + "])) / "
        "on(instance) group_left sum by (instance)((irate(node_cpu_seconds_total{instance='" + settings.instance + "', job='" + settings.job + "'}[" + settings.query_interval + "])))) * 100"
    )

    query_memory = (
        "raw_usage",
        "100 - ((node_memory_MemAvailable_bytes{instance='" + settings.instance + "', job='" + settings.job + "'} * 100) / "
        "node_memory_MemTotal_bytes{instance='" + settings.instance + "', job='" + settings.job + "'})"
    )

    query_wait = (
        "disk_wait",
        "node_pressure_io_waiting_seconds_total{instance='" + settings.instance + "', job='" + settings.job + "'} / 1000"
    )

    query_r_await = (
        "disk_read_wait",
        "rate(node_disk_read_time_seconds_total{instance='" + settings.instance + "', job='" + settings.job + "', mode!='idle'}[45s])"
    )

    query_w_await = (
        "disk_writes_wait",
        "rate(node_disk_write_time_seconds_total{instance='" + settings.instance + "', job='" + settings.job + "', mode!='idle'}[1m0s])"
    )

    query_reads_disk = (
        "disk_reads_iops",
        "irate(node_disk_reads_completed_total{instance='" + settings.instance + "', job='" + settings.job + "', mode!='idle'}[1m15s])"
    )

    query_writes_disk = (
        "disk_writes_iops",
        "irate(node_disk_writes_completed_total{instance='" + settings.instance + "', job='" + settings.job + "', mode!='idle'}[1m0s])"
    )

    query_list = [query_cpu_total_usage, query_memory, query_wait, query_r_await, query_w_await, query_reads_disk, query_writes_disk]

    for query_tuple in query_list:
        query_name, query_expression = query_tuple
        q = p.query_range(query_expression, query_start, query_end, settings.query_step)
        q.columns = [query_name]
        query_results.append(q)

    # Combine query results into a DataFrame
    df_metrics = pd.concat(query_results, axis=1)

    df_metrics['version'] = system_version
    df_metrics['operation'] = operation
    df_metrics['size'] = size    

    return df_metrics

