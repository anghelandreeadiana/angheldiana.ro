export interface Clinic {
  name: string;
  address: string;
  cas: boolean;
  phones: { label: string; href: string }[];
  website: { label: string; href: string };
}

// Source: .old/codex-version/content/locatii-si-programari.md.
export const clinics: Record<string, Clinic> = {
  "Ana Medical Care": {
    "name": "Ana Medical Care",
    "address": "Str. Brebu nr. 5, Sector 2, București",
    "cas": true,
    "phones": [
      {
        "label": "0752 443 626",
        "href": "tel:+40752443626"
      }
    ],
    "website": {
      "label": "Site-ul clinicii",
      "href": "https://anamedicalcare.ro"
    }
  },
  "Renew Institute": {
    "name": "Renew Institute",
    "address": "Str. Intrarea Căpriorilor nr. 1, Sector 1, București",
    "cas": true,
    "phones": [
      {
        "label": "0371 71 31 31",
        "href": "tel:+40371713131"
      },
      {
        "label": "sau 021 9035",
        "href": "tel:+40219035"
      }
    ],
    "website": {
      "label": "Profil profesional",
      "href": "https://renewinstitute.ro/dr-anghel-diana/"
    }
  },
  "Roua Medical Center": {
    "name": "Roua Medical Center",
    "address": "Str. Principală nr. 12, Păuleștii Noi, Prahova",
    "cas": false,
    "phones": [
      {
        "label": "0799 948 200",
        "href": "tel:+40799948200"
      }
    ],
    "website": {
      "label": "Site-ul clinicii",
      "href": "https://clinicaroua.ro/"
    }
  },
  "Angi San": {
    "name": "Angi San",
    "address": "Str. Patriei nr. 88, Buzău",
    "cas": false,
    "phones": [
      {
        "label": "0744 344 588",
        "href": "tel:+40744344588"
      }
    ],
    "website": {
      "label": "Site-ul clinicii",
      "href": "https://angisan.ro/"
    }
  },
  "Laurus Medical Buzău – Medicover": {
    "name": "Laurus Medical Buzău – Medicover",
    "address": "Bd. Stadionului nr. 7A, parter, Buzău",
    "cas": false,
    "phones": [
      {
        "label": "0371 478 888",
        "href": "tel:+40371478888"
      }
    ],
    "website": {
      "label": "Profil profesional",
      "href": "https://www.medicover.ro/medici/andreea-diana-anghel%2C4585%2Cd%2C256"
    }
  }
};
