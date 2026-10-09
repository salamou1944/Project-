# Collection recovery trigger

This marker exists only to trigger the non-recursive Collection continuous writer after its fail-closed state-guard repair.

No external source is represented by this file.

Recovery cycle: regenerate the derived queues from the preserved extraction manifest, validate every generated JSON artifact, then publish only after the fail-closed state guard passes. This trigger must not be included in extracted-source counts.
