FROM openmicroscopy/omero-server:5.6.1

ARG CERTS_DIR=/opt/omero/server/OMERO.server/certs

USER root
RUN source /opt/omero/server/venv3/bin/activate \
    && pip install omero-certificates

USER omero-server
RUN mkdir -p "${CERTS_DIR}" \
    && /opt/omero/server/OMERO.server/bin/omero config set omero.glacier2.IceSSL.DefaultDir "${CERTS_DIR}" \
    && /opt/omero/server/OMERO.server/bin/omero certificates
