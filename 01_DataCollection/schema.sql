PRAGMA encoding = 'UTF-8';
PRAGMA journal_mode = WAL;

begin transaction;

create table Vehicle
(
	gtfs_trip_id text,
	longitude float,
	latitude float,
	line_name text,
	timestamp text,
	position_state text,
	vehicle_type text
);

create table Controller
(
	id integer primary key,
	is_ready integer not null default 0
) strict;

insert into Controller default values;
update Controller set is_ready = 1;

commit;