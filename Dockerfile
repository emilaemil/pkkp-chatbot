# Perbaikan penggunaan variabel environment
ENV NIXPACKS_PATH=/opt/venv/bin:$NIXPACKS_PATH

# Perbaikan format ENV
ENV FLASK_ENV=production

# Perbaikan perintah python -m venv
RUN --mount=type=cache,id=s/a4ff7552-1bce-488f-ac91-87d9c475e03d-/root/cache/pip,target=/root/.cache/pip \
    python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install -r requirements.txt
