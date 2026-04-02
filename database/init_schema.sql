create table telemetry_log (
    id NUMBER GENERATED ALWAYS as identity primary key,
    log_timestamp timestamp default current_timestamp,
    rpm number not null,
    throttle_position number not null,
    impacted_detected number(1) default 0,
    data_hash varchar2(64) not null
);

create index idx_telemetry_time ON telemetry_log(log_timestamp);

SELECT * FROM TELEMETRY_LOG