# Backup / Sync / Disaster Recovery Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

Candidates:
- Restic — https://github.com/restic/restic
- Kopia — https://github.com/kopia/kopia
- BorgBackup — https://github.com/borgbackup/borg
- Borgmatic — https://torsion.org/borgmatic/
- Duplicati — https://github.com/duplicati/duplicati
- UrBackup — https://github.com/uroni/urbackup
- Syncthing — https://github.com/syncthing/syncthing
- Kopano — https://github.com/Kopano-dev
- MinIO/SeaweedFS/Garage for object-storage layers already captured.

Operational focus:
- encrypted backups;
- immutable/offline copies where supported;
- S3-compatible targets;
- scheduled verification;
- restore testing;
- retention and deletion policies;
- database-consistent snapshots.

A backup that has never been restored is not evidence of recoverability.
