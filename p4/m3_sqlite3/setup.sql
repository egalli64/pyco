drop table if exists country;
drop table if exists region;

-- simple: "one" region, many countries
create table region (
    region_id integer primary key,
    name varchar(25)
);

insert into region (name) values ('Europe');
insert into region (name) values ('Americas');
insert into region (name) values ('Asia');
insert into region (name) values ('Middle East and Africa');

-- a "many" table with a natural PK, to one region
create table country(
    country_id char(2) primary key,
    name varchar(40),
    region_id integer,

    constraint country_region_fk foreign key (region_id) references region (region_id)
);

insert into country (country_id, name, region_id) values ('AR', 'Argentina', 2);
insert into country (country_id, name, region_id) values ('AU', 'Australia', 3);
insert into country (country_id, name, region_id) values ('BE', 'Belgium', 1);
insert into country (country_id, name, region_id) values ('BR', 'Brazil', 2);
insert into country (country_id, name, region_id) values ('CA', 'Canada', 2);
insert into country (country_id, name, region_id) values ('CH', 'Switzerland', 1);
insert into country (country_id, name, region_id) values ('CN', 'China', 3);
insert into country (country_id, name, region_id) values ('DE', 'Germany', 1);
insert into country (country_id, name, region_id) values ('DK', 'Denmark', 1);
insert into country (country_id, name, region_id) values ('EG', 'Egypt', 4);
insert into country (country_id, name, region_id) values ('FR', 'France', 1);
insert into country (country_id, name, region_id) values ('IL', 'Israel', 4);
insert into country (country_id, name, region_id) values ('IN', 'India', 3);
insert into country (country_id, name, region_id) values ('IT', 'Italy', 1);
insert into country (country_id, name, region_id) values ('JP', 'Japan', 3);
insert into country (country_id, name, region_id) values ('KW', 'Kuwait', 4);
insert into country (country_id, name, region_id) values ('ML', 'Malaysia', 3);
insert into country (country_id, name, region_id) values ('MX', 'Mexico', 2);
insert into country (country_id, name, region_id) values ('NG', 'Nigeria', 4);
insert into country (country_id, name, region_id) values ('NL', 'Netherlands', 1);
insert into country (country_id, name, region_id) values ('SG', 'Singapore', 3);
insert into country (country_id, name, region_id) values ('UK', 'United Kingdom', 1);
insert into country (country_id, name, region_id) values ('US', 'United States of America', 2);
insert into country (country_id, name, region_id) values ('ZM', 'Zambia', 4);
insert into country (country_id, name, region_id) values ('ZW', 'Zimbabwe', 4);
