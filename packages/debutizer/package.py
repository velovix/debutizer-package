from datetime import datetime

from debutizer.binary_paragraph import BinaryParagraph
from debutizer.copyright import (
    Copyright,
    CopyrightFiles,
    CopyrightHeader,
    CopyrightLicense,
)
from debutizer.relation import PackageRelations
from debutizer.source_package import SourcePackage
from debutizer.source_paragraph import SourceParagraph
from debutizer.upstreams import SourceRepositoryUpstream
from debutizer.version import Version

_REPOSITORY_URL = "https://github.com/velovix/debutizer"
_AUTHOR = "Tyler Compton <xaviosx@gmail.com>"

upstream = SourceRepositoryUpstream(
    name="debutizer",
    version=Version.from_string("0.8.0-1"),
    repository_url=_REPOSITORY_URL,
    revision_format="v{upstream_version}",
)
package_dir = upstream.fetch()

source_package = SourcePackage(package_dir, complete=False)

source_package.set_source_format()

source_package.control.set_source(
    SourceParagraph(
        source=source_package.name,
        maintainer=_AUTHOR,
        section="utils",
        priority="optional",
        build_depends=PackageRelations.from_strings(
            [
                "debhelper",
                "dh-python",
                "python3-all",
                "python3-pytest",
                "python3-setuptools",
                "python3-debian",
                "python3-xdg",
                "python3-requests",
                "python3-flask",
                "python3-yaml",
                "s3fs",
            ]
        ),
        uploaders=[_AUTHOR],
        homepage=_REPOSITORY_URL,
    )
)
source_package.control.add_binary(
    BinaryParagraph(
        package="debutizer",
        architecture="any",
        description="A tool for managing APT packages",
        section="utils",
        priority="optional",
        depends=PackageRelations.from_strings(
            [
                "${python3:Depends}",
                "${misc:Depends}",
                "pbuilder",
                "devscripts",
                "quilt",
                "s3fs",
            ]
        ),
        recommends=PackageRelations.from_strings(
            [
                "debian-keyring",
            ]
        ),
        homepage=_REPOSITORY_URL,
    )
)

source_package.copyright.set_header(
    CopyrightHeader(
        upstream_name="debutizer",
        upstream_contact=[_AUTHOR],
        source=_REPOSITORY_URL,
        license_="BSD-3-Clause",
        copyright_="Copyright 2021 Tyler Compton",
    )
)
source_package.copyright.add_files(
    CopyrightFiles(
        files=["*", "debian/*"],
        copyright_="Copyright 2021 Tyler Compton",
        license_="BSD-3-Clause",
    )
)
source_package.copyright.add_license(
    CopyrightLicense(
        license_=Copyright.full_license_text("BSD-3-Clause"),
    )
)
source_package.set_debhelper_compat_version()

source_package.changelog.add(
    version="0.2.0-1",
    urgency="medium",
    changes=["* Initial packaging"],
    author=_AUTHOR,
    date=datetime(2021, 10, 11, 22, 46),
)

source_package.changelog.add(
    version="0.3.0-1",
    urgency="medium",
    changes=["* Add support for GPG signing"],
    author=_AUTHOR,
    date=datetime(2021, 10, 25, 22, 58),
)

source_package.changelog.add(
    version="0.4.4-1",
    urgency="medium",
    changes=[
        "* Add tools for editing package dependencies",
        "* Add cross-package dependency support",
        "* Allow configuration through environment variables",
    ],
    author=_AUTHOR,
    date=datetime(2021, 11, 4, 13, 21),
)

source_package.changelog.add(
    version="0.4.5-1",
    urgency="medium",
    changes=["* Persist changes to disk after running pre-build hooks"],
    author=_AUTHOR,
    date=datetime(2021, 11, 4, 16, 8),
)

source_package.changelog.add(
    version="0.4.6-1",
    urgency="medium",
    changes=["* Log to stderr by default"],
    author=_AUTHOR,
    date=datetime(2021, 11, 5, 12, 42),
)

source_package.changelog.add(
    version="0.5.0-1",
    urgency="medium",
    changes=[
        "* Fix Debutizer logs being buffered and coming in after subprocess logs",
        "* Make the Cache-Control header configurable for 's3-repo upload'",
        "* Add missing S3FS runtime dependency",
        "* Add missing pbuilder hook to APT releases",
        "* Start deploying to PyPI",
        "* Add a new 'check' subcommand for finding system packages",
    ],
    author=_AUTHOR,
    date=datetime(2021, 11, 5, 21, 2),
)

source_package.changelog.add(
    version="0.5.1-1",
    urgency="medium",
    changes=["* Generate S3-repo metadata using the contents of the bucket"],
    author=_AUTHOR,
    date=datetime(2021, 11, 6, 15, 12),
)

source_package.changelog.add(
    version="0.6.0-1",
    urgency="medium",
    changes=["* Migrate some configuration to a file"],
    author=_AUTHOR,
    date=datetime(2021, 11, 8, 23, 59),
)

source_package.changelog.add(
    version="0.7.0-1",
    urgency="medium",
    changes=[
        "* Third party package sources may now be added to the build environment",
        "* Source packages can now be uploaded to a PPA",
    ],
    author=_AUTHOR,
    date=datetime(2021, 11, 14, 22, 36),
)

source_package.changelog.add(
    version="0.8.0-1",
    urgency="medium",
    changes=[
        "* Do not use sudo to elevate command privileges by default",
        "* Add usage help text",
        "* Add support for S3 repo prefixes",
    ],
    author=_AUTHOR,
    date=datetime(2021, 11, 15, 0, 51),
)

source_package.complete()
