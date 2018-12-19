--
-- ViewName: error_log;
--
create view error_log as
select time::date as date, count(*) as error_count
from log
where status = '404 NOT FOUND'
group by date;

--
-- ViewName: all_log;
--
create view all_log as
select time::date as date, count(*) as all_count
from log
group by date;