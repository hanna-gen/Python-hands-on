file_path = 'data_source.json'

##############################

sql_create_tbl_for_file_src = """
        CREATE TABLE IF NOT EXISTS public.from_json_file
        (
            key character varying COLLATE pg_catalog."default",
            value numeric,
            ts character varying COLLATE pg_catalog."default"
        )

        TABLESPACE pg_default;

        ALTER TABLE IF EXISTS public.from_json_file
            OWNER to postgres;
    """

sql_insert_tbl_for_file_src = """
        INSERT INTO public.from_json_file(key, value, ts)
        VALUES(%s, %s, %s)
    """

sql_create_tbl_for_simul_src = """
        CREATE TABLE IF NOT EXISTS public.from_simul_src
        (
            pk INTEGER,
            rnd_data character varying COLLATE pg_catalog."default"
        )

        TABLESPACE pg_default;

        ALTER TABLE IF EXISTS public.from_simul_src
            OWNER to postgres;
    """

sql_insert_tbl_for_simul_src = """
        INSERT INTO public.from_simul_src(pk, rnd_data)
        VALUES(%s, %s)
    """

sql_max_pk_for_simul_src = """
        select max(pk) from public.from_simul_src
    """
