querys = [
    
    """
    DROP TABLE IF EXISTS public.usuario
    """,
    """
    DROP TABLE IF EXISTS public."exposicionCultural"
    """,
    """
    DROP TABLE IF EXISTS public.evento
    """,
    """
    DROP TABLE IF EXISTS public.menu
    """,
    """
    DROP TABLE IF EXISTS public."tierraYSazon"
    """,
  
    """
        CREATE TABLE IF NOT EXISTS public.usuario
        (
            id serial NOT NULL,
            nombre character(20) COLLATE pg_catalog."default" NOT NULL,
            contra character(30) COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT usuario_pkey PRIMARY KEY (id)
        )
    """,
    """
    CREATE TABLE IF NOT EXISTS public."tierraYSazon"
        (
            "idSucursal" serial NOT NULL,
            direccion character(60) COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT "tierraYSazon_pkey" PRIMARY KEY ("idSucursal")
        )
    """
    ,

    """
        CREATE TABLE IF NOT EXISTS public.menu
        (
            "idMenu" serial NOT NULL,
            nombre character(45) COLLATE pg_catalog."default" NOT NULL,
            tipo character(20) COLLATE pg_catalog."default" NOT NULL,
            precio integer NOT NULL,
            descripcion character(45) COLLATE pg_catalog."default" NOT NULL,
            cultura character(45) COLLATE pg_catalog."default" NOT NULL,
            "tierraYSazon_idSucursal" integer NOT NULL,
            CONSTRAINT menu_pkey PRIMARY KEY ("idMenu"),
            CONSTRAINT "FK_MENU_TIERRA" FOREIGN KEY ("tierraYSazon_idSucursal")
                REFERENCES public."tierraYSazon" ("idSucursal") MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
                NOT VALID
        )
    """
    ,
    """
        CREATE TABLE IF NOT EXISTS public.evento
        (
            "idEvento" serial NOT NULL,
            nombre character(45) COLLATE pg_catalog."default",
            descripcion character(500) COLLATE pg_catalog."default" NOT NULL,
            fecha date NOT NULL,
            imagen bytea,
            "tierraYSazon_idSucursal" integer NOT NULL,
            CONSTRAINT evento_pkey PRIMARY KEY ("idEvento"),
            CONSTRAINT "FK_EVENTO_TIERRA" FOREIGN KEY ("tierraYSazon_idSucursal")
                REFERENCES public."tierraYSazon" ("idSucursal") MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
        )
    """
    ,
    """
        CREATE TABLE IF NOT EXISTS public."exposicionCultural"
            (
                "idExposicionCultural" serial NOT NULL,
                nombre character(45) COLLATE pg_catalog."default",
                descripcion character(500) COLLATE pg_catalog."default" NOT NULL,
                fecha date NOT NULL,
                imagen bytea,
                "tierraYSazon_idSucursal" integer NOT NULL,
                CONSTRAINT "exposicionCultural_pkey" PRIMARY KEY ("idExposicionCultural"),
                CONSTRAINT "FK_EXPOSICION_CULTURAL" FOREIGN KEY ("tierraYSazon_idSucursal")
                    REFERENCES public."tierraYSazon" ("idSucursal") MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
            )
    """,
    """
        INSERT INTO public.usuario (nombre, contra) values
        ('carlos','12345')
    """
    ,
    """
        INSERT INTO public.usuario (nombre, contra) values
        ('osmar','12345')
    """
    ,
    """
        INSERT INTO public.usuario (nombre, contra) values
        ('santiago','12345')
    """
    
    ,
    
    """
        INSERT INTO public."tierraYSazon" (direccion) values
        ('calle falsa 123')
    """
    ,
    
    """
        INSERT INTO public.menu (nombre, tipo, precio, descripcion, cultura,"tierraYSazon_idSucursal") values
        ('pozole','platillo',70, 'El platillo favorito de los mexicanos', 'Mexica',1)
    """,
    """
    INSERT INTO public.menu (nombre,tipo,precio,descripcion,cultura, "tierraYSazon_idSucursal") values
    ('quesadilla azul','comida',60,'unas ricas quesadillas azules','cora',1),
    ('gorditas','comida',70,'unas ricas gorditas','huichol',1)
    """,
    """
    INSERT INTO public."exposicionCultural" (descripcion,fecha,imagen,"tierraYSazon_idSucursal")
    values ('banda cora','2023/7/1',null,1),
    ('banda huichol','2023/7/1',null,1)
    """,
    """
    INSERT INTO public.evento (descripcion,fecha,imagen,"tierraYSazon_idSucursal")
    values ('banda cora','2023/7/1',null,1),
    ('banda huichol','2023/7/1',null,1)
    """,
    
    """
    UPDATE public.evento 
    SET nombre = 'Banda cora'
    WHERE "idEvento" = 1
    """,
     """
    UPDATE public.evento 
    SET nombre = 'Banda MS'
    WHERE "idEvento" = 2
    """,
    
     """
    UPDATE public."exposicionCultural"
    SET nombre = 'Mexica'
    WHERE "idExposicionCultural" = 1
    """,
    
    """
    UPDATE public."exposicionCultural"
    SET nombre = 'Maya'
    WHERE "idExposicionCultural" = 2
    """,
    """
    DELETE FROM public.evento
    WHERE "idEvento" >=7 AND "idEvento" <=30
    """
    ,
    """
    INSERT INTO public.menu (nombre,tipo,descripcion,precio,cultura,"tierraYSazon_idSucursal") values
    ('Tejuino','Bebida','ef',60,'cora',1)
    """,
    """
    INSERT INTO public.menu (nombre,tipo,descripcion,precio, cultura,"tierraYSazon_idSucursal") values
    ('Menudo','Platillo','ef',60,'cora',1)
    """,
    """
    INSERT INTO public.menu (nombre,tipo,descripcion,precio,cultura,"tierraYSazon_idSucursal") values
    ('Papas','Entrada','ef',60,'cora',1)
    """,
    """
    INSERT INTO public.menu (nombre,tipo,descripcion, precio,cultura,"tierraYSazon_idSucursal") values
    ('Helado cora xD','Postre','ef',60,'cora',1)
    """
    
]