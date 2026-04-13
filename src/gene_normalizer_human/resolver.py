import difflib

class GeneResolver:
    def __init__(self, gene_name_to_ids, gene_id_to_name, synonym_map=None):
        self.gene_name_to_ids = gene_name_to_ids
        self.gene_id_to_name = gene_id_to_name
        self.synonym_map = synonym_map or {}
        self._universe = set(gene_name_to_ids.keys()) | set(self.synonym_map.keys())

    def resolve_one(self, token: str, fuzzy=True, cutoff=0.86):
        key = token.strip().lower()
        if not key:
            return None
        # Synonym exact
        if key in self.synonym_map:
            canonical = self.synonym_map[key]
            ids = self.gene_name_to_ids.get(canonical.lower(), set())
            if ids:
                gid_list = sorted(ids)
                proper = canonical
                return {"token": token, "matched_symbol": proper, "ensembl_gene_id": ";".join(gid_list), "match_type": "synonym-exact"}
            return {"token": token, "matched_symbol": canonical, "ensembl_gene_id": "", "match_type": "synonym-only"}
        # Gene name exact
        if key in self.gene_name_to_ids:
            ids = self.gene_name_to_ids[key]
            gid_list = sorted(ids)
            proper = self.gene_id_to_name[gid_list[0]]
            return {"token": token, "matched_symbol": proper, "ensembl_gene_id": ";".join(gid_list), "match_type": "name-exact"}
        # Fuzzy
        if fuzzy and self._universe:
            cand = difflib.get_close_matches(key, list(self._universe), n=1, cutoff=cutoff)
            if cand:
                ck = cand[0]
                if ck in self.synonym_map:
                    canonical = self.synonym_map[ck]
                    ids = self.gene_name_to_ids.get(canonical.lower(), set())
                    gid_list = sorted(ids)
                    return {"token": token, "matched_symbol": canonical, "ensembl_gene_id": ";".join(gid_list), "match_type": "fuzzy-synonym"}
                if ck in self.gene_name_to_ids:
                    ids = self.gene_name_to_ids[ck]
                    gid_list = sorted(ids)
                    proper = self.gene_id_to_name[gid_list[0]]
                    return {"token": token, "matched_symbol": proper, "ensembl_gene_id": ";".join(gid_list), "match_type": "fuzzy-name"}
        return {"token": token, "matched_symbol": "", "ensembl_gene_id": "", "match_type": "unmatched"}
