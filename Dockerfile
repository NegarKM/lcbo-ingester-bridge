ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
ENV VENV_PATH=/app/.venv

WORKDIR /app

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


RUN pip install --upgrade pip==24.0 \
    && pip install pipenv

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
#--mount=type=cache,target=~/Library/Caches/pipenv \
RUN --mount=type=bind,source=./Pipfile,target=Pipfile \
    PIPENV_VENV_IN_PROJECT=1 pipenv install

COPY src src
COPY start.sh start.sh

USER appuser

EXPOSE 8000

CMD ["/bin/bash"]

#ENTRYPOINT ["./start.sh"]
#CMD ["2023-12-14"]
