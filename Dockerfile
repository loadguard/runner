# # Dockerfile for: transilien.pubct.loadtests

FROM registry-docker.apps.eul.sncf.fr/hub/python:3.9-slim-buster as builder

WORKDIR "/app"

COPY [".docker/adds/", "/"]
COPY ["/src", "/app/src"]
COPY ["requirements.txt", "/app/"]

RUN pip3 install -r requirements.txt \
    && chmod +x /opt/docker-entrypoint.sh

FROM scratch

ENV LD_LIBRARY_PATH "/lib64:/usr/lib:/usr/local/lib"
ENV PYTHON_HOME "/usr/local/bin"
ENV PYTHONPATH "${PYTHONPATH}:/app/lib/runner/src:/app/lib/python-sandbox-inprogress/src:/app/lib/transilien-fid-auth/src:/app/project"
ENV PYTHONUNBUFFERED "0"

COPY --from=python-image ["/", "/"]
COPY --from=builder ["/root/.config", "/root/.config"]
COPY --from=builder ["/app", "/app"]
COPY --from=builder ["/opt", "/opt"]
COPY --from=builder ["/usr/local/lib/python3.9/site-packages", "/usr/local/lib/python3.9/site-packages"]

ENTRYPOINT ["/opt/docker-entrypoint.sh"]
CMD ["/usr/local/bin/python3", "/app/lib/runner/src/loadguard/main.py"]
