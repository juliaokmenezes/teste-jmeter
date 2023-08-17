from datetime import datetime
import os
from generate_df import new_node_exporter_metrics_df
import settings

version_dict = {
    'LocalStorage': {
        '4': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 10, 13),
                'query_end': datetime(2023, 7, 18, 19, 10, 48),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 19, 10, 48),
                'query_end': datetime(2023, 7, 18, 19, 11, 50),
            }
        },
        '8': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 12, 0),
                'query_end': datetime(2023, 7, 18, 19, 13, 0),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 19, 13, 0),
                'query_end': datetime(2023, 7, 18, 19, 14, 25),
            }
        },
        '16': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 14, 35),
                'query_end': datetime(2023, 7, 18, 19, 16, 30),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 19, 16, 30),
                'query_end': datetime(2023, 7, 18, 19, 18, 25),
            }
        },
        '32': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 16, 35),
			    'query_end': datetime(2023, 7, 18, 19, 22, 15),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 19, 22, 20),
                'query_end': datetime(2023, 7, 18, 19, 25, 20),
        }},
        '64': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 25, 30),
                'query_end': datetime(2023, 7, 18, 19, 32, 10),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 19, 32, 15),
                'query_end': datetime(2023, 7, 18, 19, 37, 25),   
        }},
        '128': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 37, 40),
                'query_end': datetime(2023, 7, 18, 19, 49, 55),
            },
            'Download':{
                'query_start': datetime(2023, 7, 18, 19, 50, 5),
                'query_end': datetime(2023, 7, 18, 19, 59, 30),
        }},
        '256': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 19, 59, 55),
                'query_end': datetime(2023, 7, 18, 20, 23, 20),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 20, 23, 45),
                'query_end': datetime(2023, 7, 18, 20, 42, 5),
    }}},
    'S3': {
        '4': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 20, 43, 10),
                'query_end': datetime(2023, 7, 18, 20, 44, 0),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 20, 44, 0),
                'query_end': datetime(2023, 7, 18, 20, 45, 5),
            }
        },
        '8': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 20, 45, 15),
                'query_end': datetime(2023, 7, 18, 20, 46, 40),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 20, 46, 40),
                'query_end': datetime(2023, 7, 18, 20, 48, 10),
            }
        },
        '16': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 20, 48, 20),
                'query_end': datetime(2023, 7, 18, 20, 50, 40),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 20, 50, 40),
                'query_end': datetime(2023, 7, 18, 20, 52, 40),
            }
        },
        '32': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 20, 52, 55),
			    'query_end': datetime(2023, 7, 18, 20, 57, 15),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 20, 57, 20),
                'query_end': datetime(2023, 7, 18, 21, 0, 40),
        }},
        '64': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 21, 0, 50),
                'query_end': datetime(2023, 7, 18, 21, 8, 20),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 21, 8, 20),
                'query_end': datetime(2023, 7, 18, 21, 14, 10),   
        }},
        '128': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 21, 14, 30),
                'query_end': datetime(2023, 7, 18, 21, 27, 45),
            },
            'Download':{
                'query_start': datetime(2023, 7, 18, 21, 27, 55),
                'query_end': datetime(2023, 7, 18, 21, 38, 35),
        }},
        '256': {
            'Upload': {
                'query_start': datetime(2023, 7, 18, 21, 39, 0),
                'query_end': datetime(2023, 7, 18, 22, 4, 10),
            },
            'Download': {
                'query_start': datetime(2023, 7, 18, 22, 4, 40),
                'query_end': datetime(2023, 7, 18, 22, 25, 10),
    }}}
}

OUTPUT_DIRECTORY_PATH = './stress-testing-nutbox/logs/results/server/'

COLUMNS_METRICS = [
                'version', 'operation', 'size', 'cpu_iowait_usage', 'cpu_softirq_usage',
                'cpu_steal_usage', 'cpu_system_usage', 'cpu_user_usage', 'cpu_total_usage', 'raw_usage',
                'disk_wait', 'disk_read_wait', 'disk_writes_wait', 'disk_reads_iops', 'disk_writes_iops']

def create_logs(version_dict):
    default_settings = settings.LogSettings.default()
    for v in version_dict:
        size_dict = version_dict[v]
        for s in size_dict:
            operation_dict = size_dict[s]
            to_concatenate = []
            
            for op in operation_dict:
                query_dict = operation_dict[op]
                q_s, q_e = query_dict['query_start'], query_dict['query_end']
                df_op = new_node_exporter_metrics_df(default_settings, q_s, q_e, v, op, s)
                to_concatenate.append(df_op)
            
            df_completed = pd.concat(to_concatenate)
            if v == 'LocalStorage':
                tag_version = 'LS'
            else:
                tag_version = 'S3'
            df_completed.to_csv(os.path.join(OUTPUT_DIRECTORY_PATH, f'{tag_version}_{s}MB.csv'), sep=',', header=True, index=True, index_label='timeStamp', columns=COLUMNS_METRICS, date_format = '%Y-%m-%d %H:%M:%S.%f', decimal='.')
 
create_logs(version_dict)
