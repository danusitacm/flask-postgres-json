
CREATE SEQUENCE public.materia_materia_pk_seq;

CREATE TABLE public.materia (
                materia_pk BIGINT NOT NULL DEFAULT nextval('public.materia_materia_pk_seq'),
                nombre VARCHAR NOT NULL,
                codigo VARCHAR NOT NULL,
                CONSTRAINT materia_pk PRIMARY KEY (materia_pk)
);


ALTER SEQUENCE public.materia_materia_pk_seq OWNED BY public.materia.materia_pk;

CREATE SEQUENCE public.usuario_usuario_pk_seq;

CREATE TABLE public.usuario (
                usuario_pk BIGINT NOT NULL DEFAULT nextval('public.usuario_usuario_pk_seq'),
                nombre VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                telefono VARCHAR(255) NOT NULL,
                genero VARCHAR(255) NOT NULL,
                CONSTRAINT usuario_pk PRIMARY KEY (usuario_pk)
);


ALTER SEQUENCE public.usuario_usuario_pk_seq OWNED BY public.usuario.usuario_pk;

CREATE SEQUENCE public.tutor_tutor_pk_seq;

CREATE TABLE public.tutor (
                tutor_pk BIGINT NOT NULL DEFAULT nextval('public.tutor_tutor_pk_seq'),
                puntaje_tutor REAL NOT NULL,
                usuario_pk BIGINT NOT NULL,
                CONSTRAINT tutor_pk PRIMARY KEY (tutor_pk)
);


ALTER SEQUENCE public.tutor_tutor_pk_seq OWNED BY public.tutor.tutor_pk;

CREATE TABLE public.tutor_materia (
                materia_pk BIGINT NOT NULL,
                tutor_pk BIGINT NOT NULL,
                CONSTRAINT tutor_materia_pk PRIMARY KEY (materia_pk, tutor_pk)
);


CREATE SEQUENCE public.alumno_alumno_pk_seq;

CREATE TABLE public.alumno (
                alumno_pk BIGINT NOT NULL DEFAULT nextval('public.alumno_alumno_pk_seq'),
                puntaje_alumno REAL NOT NULL,
                usuario_pk BIGINT NOT NULL,
                CONSTRAINT alumno_pk PRIMARY KEY (alumno_pk)
);


ALTER SEQUENCE public.alumno_alumno_pk_seq OWNED BY public.alumno.alumno_pk;

CREATE SEQUENCE public.review_alumno_review_alumno_pk_seq;

CREATE TABLE public.review_alumno (
                review_alumno_pk BIGINT NOT NULL DEFAULT nextval('public.review_alumno_review_alumno_pk_seq'),
                descripcion VARCHAR(255) NOT NULL,
                calificacion_alumno INTEGER DEFAULT 0 NOT NULL,
                alumno_pk BIGINT NOT NULL,
                tutor_pk BIGINT NOT NULL,
                CONSTRAINT review_alumno_pk PRIMARY KEY (review_alumno_pk)
);


ALTER SEQUENCE public.review_alumno_review_alumno_pk_seq OWNED BY public.review_alumno.review_alumno_pk;

CREATE TABLE public.review_tutor (
                review_tutor_pk BIGINT NOT NULL,
                descripcion VARCHAR NOT NULL,
                calificacion_tutor INTEGER DEFAULT 0 NOT NULL,
                alumno_pk BIGINT NOT NULL,
                tutor_pk BIGINT NOT NULL,
                CONSTRAINT review_tutor_pk PRIMARY KEY (review_tutor_pk)
);


CREATE SEQUENCE public.tutoria_tutoria_pk_seq;

CREATE TABLE public.tutoria (
                tutoria_pk BIGINT NOT NULL DEFAULT nextval('public.tutoria_tutoria_pk_seq'),
                fecha_inicio DATE NOT NULL,
                fecha_fin DATE NOT NULL,
                materia_pk BIGINT NOT NULL,
                alumno_pk BIGINT NOT NULL,
                tutor_pk BIGINT NOT NULL,
                CONSTRAINT tutoria_pk PRIMARY KEY (tutoria_pk)
);


ALTER SEQUENCE public.tutoria_tutoria_pk_seq OWNED BY public.tutoria.tutoria_pk;

CREATE SEQUENCE public.solicitud_solicitud_pk_seq;

CREATE TABLE public.solicitud (
                solicitud_pk BIGINT NOT NULL DEFAULT nextval('public.solicitud_solicitud_pk_seq'),
                fecha_solicitud DATE NOT NULL,
                estado_solicitud VARCHAR NOT NULL,
                materia_pk BIGINT NOT NULL,
                alumno_pk BIGINT NOT NULL,
                CONSTRAINT solicitud_pk PRIMARY KEY (solicitud_pk)
);


ALTER SEQUENCE public.solicitud_solicitud_pk_seq OWNED BY public.solicitud.solicitud_pk;

ALTER TABLE public.tutor_materia ADD CONSTRAINT materia_tutor_materia_fk
FOREIGN KEY (materia_pk)
REFERENCES public.materia (materia_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tutoria ADD CONSTRAINT materia_tutoria_fk
FOREIGN KEY (materia_pk)
REFERENCES public.materia (materia_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.solicitud ADD CONSTRAINT materia_solicitud_fk
FOREIGN KEY (materia_pk)
REFERENCES public.materia (materia_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.alumno ADD CONSTRAINT usuario_alumno_fk
FOREIGN KEY (usuario_pk)
REFERENCES public.usuario (usuario_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tutor ADD CONSTRAINT usuario_tutor_fk
FOREIGN KEY (usuario_pk)
REFERENCES public.usuario (usuario_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tutor_materia ADD CONSTRAINT tutor_tutor_materia_fk
FOREIGN KEY (tutor_pk)
REFERENCES public.tutor (tutor_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tutoria ADD CONSTRAINT tutor_tutoria_fk
FOREIGN KEY (tutor_pk)
REFERENCES public.tutor (tutor_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.review_tutor ADD CONSTRAINT tutor_review_tutor_fk
FOREIGN KEY (tutor_pk)
REFERENCES public.tutor (tutor_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.review_alumno ADD CONSTRAINT tutor_review_alumno_fk
FOREIGN KEY (tutor_pk)
REFERENCES public.tutor (tutor_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.solicitud ADD CONSTRAINT alumno_solicitud_fk
FOREIGN KEY (alumno_pk)
REFERENCES public.alumno (alumno_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tutoria ADD CONSTRAINT alumno_tutoria_fk
FOREIGN KEY (alumno_pk)
REFERENCES public.alumno (alumno_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.review_tutor ADD CONSTRAINT alumno_review_tutor_fk
FOREIGN KEY (alumno_pk)
REFERENCES public.alumno (alumno_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.review_alumno ADD CONSTRAINT alumno_review_alumno_fk
FOREIGN KEY (alumno_pk)
REFERENCES public.alumno (alumno_pk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;