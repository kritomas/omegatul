PRAGMA encoding = 'UTF-8';
PRAGMA journal_mode = WAL;

begin transaction;

create table Controller
(
	id integer primary key,
	is_ready integer not null default 0
) strict;

insert into Controller default values;
update Controller set is_ready = 1;

commit;